from django.contrib import admin
from infinite.models import Category, Page
from infinite.models import UserProfile

class PageAdmin(admin.ModelAdmin):
    list_display = ('title','category','url')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    
admin.site.register(Category)
admin.site.register(Page,PageAdmin)
admin.site.register(UserProfile)

