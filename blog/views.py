from django.shortcuts import render
from django.views.generic import View, DetailView


class BaseView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'base.html', {})


class CategoryDetailView(DetailView):
    """View of one specific category"""
    context_object_name = 'category'
    template_name = 'category_detail.html'
    slug_url_kwarg = 'slug'


class PostDetailView(DetailView):
    """View of one specific post"""
    context_object_name = 'post'
    template_name = 'post_detail.html'
    slug_url_kwarg = 'slug'

