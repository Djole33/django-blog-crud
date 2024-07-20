from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
	    return self.name

    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    title = models.CharField(max_length=255) 
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #ovo znaci kada se obrise user, brisu se svi njegovi blogovi
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True) #auto_now_add - datum se automatski dodaje da ne bi user pisao kad je napravio post
    category = models.CharField(max_length=255, default='coding')

    def __str__(self):
	    return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')
    