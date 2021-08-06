from django.urls import path
from infinite import views

app_name = 'infinite'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('myaccount/', views.myaccount, name='myaccount'),
    path('myaccount/likelist/', views.likelist, name='likelist'),
    path('category/<slug:category_name_slug>/',views.show_category, name='show_category'),
    path('category/<slug:category_name_slug>/add_game/',views.add_game, name='add_game'),
    path('category/<slug:category_name_slug>/<slug:game_name_slug>/',views.show_game, name='show_game'),
    path('add_category/', views.add_category, name='add_category'),
    path('search/<query>', views.search, name='search'),
    path('like_game/', views.LikeGameView.as_view(), name='like_game'),
]
