from datetime import datetime
from django.db import models
from django.template.defaultfilters import default, slugify
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(blank=True,unique=True)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super(Category,self).save(*args,**kwargs)
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    picture = models.ImageField(upload_to='profile_images', blank=True)
    def __str__(self):
        return self.user.username

class Game(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(blank=True,unique=True)
    released_date = models.DateField(default=datetime.now)
    description = models.CharField(max_length=1000)
    picture = models.ImageField(upload_to='images', blank=True)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super(Game,self).save(*args,**kwargs)

    def __str__(self):
        return self.name

class Comment(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    date =  models.DateField(default=datetime.now)

class Like_List(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    game = models.ManyToManyField(Game,blank=True)
