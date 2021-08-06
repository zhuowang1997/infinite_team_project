from django import forms
from django.forms.widgets import DateTimeBaseInput, DateTimeInput
from django.http import request
from django.template.defaultfilters import default
from infinite.models import Game, Category,Comment
from django.contrib.auth.models import User
from infinite.models import UserProfile

#form of Category, user need to input name when adding new category.
class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128,
                help_text="Please enter the category name.")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name',)

#form of Game, user need to input name, release date, description of the game, and upload an image when adding new category.
class GameForm(forms.ModelForm):
    name = forms.CharField(max_length=128,
                help_text="Please enter the name of the game.")
    released_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}),
                help_text="Please enter the released date of the game.")

    description = forms.CharField(widget=forms.Textarea,
                help_text="Please enter the description of the game.")

    picture = forms.ImageField(
                help_text="Please upload an image.")
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Game
        exclude = ('category',)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

 #user form for uploading personal profile image in profile page
class UserProfileForm(forms.ModelForm):
    picture = forms.ImageField(
                help_text="Please upload your profile photo.")
         
    class Meta:
        model = UserProfile
        fields = ('picture',)

#comment form for inputing comments in game page.
class CommentForm(forms.ModelForm):
    comment = forms.CharField(max_length=500, widget=forms.Textarea,
               help_text="Please enter your comment." )
    class Meta:
        model = Comment
        fields = ('comment',)

    
