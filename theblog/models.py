from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
	    return self.name

    def get_absolute_url(self):
        return reverse('home')

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(max_length=255, null=True, blank=True)
    website_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url= models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    pinterest_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
	    return str(self.user)

class Post(models.Model):
    title = models.CharField(max_length=255) 
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #ovo znaci kada se obrise user, brisu se svi njegovi blogovi
    body = RichTextField(blank=True, null=True)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    # body = models.TextField()
    post_date = models.DateField(auto_now_add=True) #auto_now_add - datum se automatski dodaje da ne bi user pisao kad je napravio post
    category = models.CharField(max_length=255, default='coding')
    likes = models.ManyToManyField(User, related_name="blog_posts") # related_name je kao ForeignKey
    snippets = models.CharField(max_length=255)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
	    return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')
