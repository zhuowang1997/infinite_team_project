from django.shortcuts import render,redirect
from django.http import HttpResponse
from infinite.models import Category,Game,Comment,Like_List
from infinite.forms import CategoryForm,GameForm,UserForm, UserProfileForm,CommentForm
from django.urls import reverse
from django.contrib.auth import authenticate, get_user_model, login,logout
from django.contrib.auth.decorators import login_required
from datetime import datetime

def index(request):
    category_list = Category.objects.all
    games_list = Game.objects.order_by('-likes')[:5]

    context_dict = {}
    context_dict['categories'] = category_list
    context_dict['games'] = games_list

    request.session.set_test_cookie()

    visitor_cookie_handler(request)

    response = render(request, 'infinite/index.html', context=context_dict)
    # Call the helper function to handle the cookies

    # Return response back to the user, updating any cookies that need changed.
    return response

@login_required
def myaccount(request):

    response = render(request, 'infinite/myaccount.html')

    return response

@login_required
def likelist(request):
    user = request.user
    likelist = Like_List.objects.get(user = user)
    games = likelist.game.all()
    context_dict = {}
    context_dict['games'] = games
    response = render(request, 'infinite/likelist.html',context_dict)

    return response

def about(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage matches to {{ boldmessage }} in the template!
    context_dict = {}

    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    return render(request, 'infinite/about.html', context=context_dict)


def show_category(request, category_name_slug):
    # Create a context dictionary which we can pass
    # to the template rendering engine.
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        games = Game.objects.filter(category=category)

        context_dict['games'] = games
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['games'] = None

    return render(request, 'infinite/category.html', context=context_dict)

def show_game(request, category_name_slug,game_name_slug):
    # Create a context dictionary which we can pass
    # to the template rendering engine.
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
    return render(request, 'infinite/game.html', context=context_dict)


@login_required
def add_category(request):
    form = CategoryForm()
    # A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)
            # Now that the category is saved, we could confirm this.
            # For now, just redirect the user back to the index view.
            return redirect('/infinite/')
        else:
            # The supplied form contained errors -
            # just print them to the terminal.
            print(form.errors)
    # Will handle the bad form, new form, or no form supplied cases.
    # Render the form with error messages (if any).
    return render(request, 'infinite/add_category.html', {'form': form})


@login_required
def add_game(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None
    # You cannot add a game to a Category that does not exist...
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
    return render(request, 'infinite/add_game.html', context=context_dict)

@login_required
def restricted(request):
    return render(request, 'infinite/restricted.html')

# A helper method
def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val
    # Updated the function definition

def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request,'last_visit',str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7],
    '%Y-%m-%d %H:%M:%S')
    # If it's been more than a day since the last visit...
    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        # Update the last visit cookie now that we have updated the count
        request.session['last_visit'] = str(datetime.now())
    else:
        # Set the last visit cookie
        request.session['last_visit'] = last_visit_cookie
    # Update/set the visits cookie
    request.session['visits'] = visits