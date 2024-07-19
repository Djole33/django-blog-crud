from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView #list view pretrazuje databazu i daje listu postova, a detail daje 1 post
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

# Create your views here.

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category = cats.replace('-', ' '))
    return render(request, 
                  'categories.html', 
                  {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date'] # blog postovi su poredjani po ID-u pravljenja dok ne dodam datum
    # ordering = ['-id'] # blog postovi su poredjani po ID-u pravljenja dok ne dodam datum

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = "__all__"

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    # fields = ['title', 'title_tag', 'body'] # mogu koristiti i fields umesto form_class ako ne zelim da pravim formu u forms.py

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home') # ovo je za redirect na home page nakon klika na dugme Delete
