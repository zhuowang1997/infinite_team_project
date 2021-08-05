from django.contrib import admin
from infinite.models import Category, Game,Comment,Like_List
from infinite.models import UserProfile

class GameAdmin(admin.ModelAdmin):
    list_display = ('name','category','released_date')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    
admin.site.register(Category)
admin.site.register(Game,GameAdmin)
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(Like_List)
