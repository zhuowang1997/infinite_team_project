from django.shortcuts import render,redirect
from infinite.models import Category,Game,Comment,Like_List,UserProfile
from infinite.forms import CategoryForm,GameForm, CommentForm,UserProfileForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views import View
from django.utils.decorators import method_decorator

def index(request):
    category_list = Category.objects.all
    games_list = Game.objects.order_by('-likes')[:5]

    context_dict = {}
    context_dict['categories'] = category_list
    context_dict['games'] = games_list

    if request.method == 'POST':
        query = request.POST['query'].strip()
        if query:
            return redirect(reverse('infinite:search', kwargs={'query': query}))

    response = render(request, 'infinite/index.html', context=context_dict)

    return response

def search(request, query):
    result_list = []

    if request.method == 'POST':
        query = request.POST['query'].strip()
        
    if query:
        result_list = Game.objects.filter(name__icontains=query).all()
    
    category_list = Category.objects.all
    context_dict = {}
    context_dict['categories'] = category_list
    context_dict['result_list'] = result_list
        
    return render(request, 'infinite/search.html', context=context_dict)

@login_required
def myaccount(request):

    user = request.user
    form = UserProfileForm()
    try:
        profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        profile = form.save(commit=False)
        profile.user = user
        profile.save()
    if request.method == 'POST':
        form = UserProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile_cd = form.cleaned_data
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            return redirect('/infinite/myaccount/')
        else:
            print(form.errors)
    
    context_dict = {'form': form,'profile':profile}
    category_list = Category.objects.all
    context_dict['categories'] = category_list
    return render(request, 'infinite/myaccount.html', context=context_dict)


@login_required
def likelist(request):

    user = request.user
    context_dict = {}
    try:
        likelist = Like_List.objects.get(user = user)
        games = likelist.game.all()
        context_dict['games'] = games
    except Like_List.DoesNotExist:
        context_dict['games'] = None

    category_list = Category.objects.all
    context_dict['categories'] = category_list

    response = render(request, 'infinite/likelist.html',context_dict)

    return response


def about(request):

    context_dict = {}
    category_list = Category.objects.all
    context_dict['categories'] = category_list

    return render(request, 'infinite/about.html', context_dict)


def show_category(request, category_name_slug):

    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        games = Game.objects.filter(category=category)

        context_dict['games'] = games
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['games'] = None
    
    category_list = Category.objects.all
    context_dict['categories'] = category_list

    return render(request, 'infinite/category.html', context=context_dict)

def show_game(request, category_name_slug,game_name_slug):

    form = CommentForm()
    context_dict = {}
    try:
        game = Game.objects.get(slug=game_name_slug)
        comments = Comment.objects.filter(game=game)
        category = game.category
        context_dict['category'] = category
        context_dict['game'] = game
        context_dict['comments'] = comments
    except Game.DoesNotExist:
        context_dict['game'] = None
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.game = game
            comment.save()
            return redirect(reverse('infinite:show_game',
                                        kwargs={'category_name_slug':
                                        category_name_slug,
                                                'game_name_slug':
                                        game_name_slug}))
        else:
            print(form.errors)
        context_dict['form'] = form

    category_list = Category.objects.all
    context_dict['categories'] = category_list

    return render(request, 'infinite/game.html', context=context_dict)


@login_required
def add_category(request):
    form = CategoryForm()
    
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        
        if form.is_valid():
            
            form.save(commit=True)
            
            return redirect('/infinite/')
        else:
           
            print(form.errors)
    
    context_dict = {}
    context_dict['form'] = form
    category_list = Category.objects.all
    context_dict['categories'] = category_list
   
    return render(request, 'infinite/add_category.html', context_dict)


@login_required
def add_game(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None
    
    if category is None:
        return redirect(reverse('infinite:index'))
    form = GameForm()
    if request.method == 'POST':
        form = GameForm(request.POST,request.FILES)
        if form.is_valid():
            if category:
                game = form.save(commit=False)
                game.category = category
                game.save()
                return redirect(reverse('infinite:show_category',
                                        kwargs={'category_name_slug':
                                        category_name_slug}))
        else:
            print(form.errors)
    context_dict = {'form': form, 'category': category}
    category_list = Category.objects.all
    context_dict['categories'] = category_list
    
    return render(request, 'infinite/add_game.html', context=context_dict)

class LikeGameView(View):
    @method_decorator(login_required)
    def get(self, request):
        user = request.user
        game_id = request.GET.get('game_id')
        try:
            game = Game.objects.get(id=int(game_id))
            likelist,created=Like_List.objects.get_or_create(user=user)
        except Game.DoesNotExist:
            return HttpResponse(-1)
        except ValueError:
            return HttpResponse(-1)
        if not Like_List.objects.filter(game=game,user=user):
            likelist.game.add(game)
            game.likes = game.likes + 1
            game.save()
            likelist.save()

        return HttpResponse(game.likes)    
