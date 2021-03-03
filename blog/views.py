from django.shortcuts import render
from django.views.generic import View, DetailView, ListView

from blog.models import Category, Post
from blog.services import get_posts_for_main_page


class BaseView(View):
    """Main page view"""

    def get(self, request, *args, **kwargs):
        main_posts = get_posts_for_main_page()
        context = {
            'posts': main_posts
        }
        return render(request, 'base.html', context)


class AboutView(View):
    """View with information about firm"""

    def get(self, request, *args, **kwargs):
        return render(request, 'about.html', {})


class ProjectsView(ListView):
    """View with all posts"""
    model = Post
    context_object_name = 'Post'
    queryset = Post.objects.all()
    template_name = 'post_list.html'


class CategoryDetailView(DetailView):
    """View of one specific category"""
    model = Category
    context_object_name = 'category'
    template_name = 'category_detail.html'
    slug_url_kwarg = 'slug'


class PostDetailView(DetailView):
    """View of one specific post"""
    model = Post
    context_object_name = 'post'
    template_name = 'post_detail.html'
    slug_url_kwarg = 'slug'
