from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View, DetailView, ListView

from blog.models import Post
from blog.services import get_posts_for_main_page
from question.forms import QuestionForm


class BaseView(View):
    """Main page view"""

    def get(self, request, *args, **kwargs):
        main_posts = get_posts_for_main_page()
        form = QuestionForm()
        context = {
            'posts': main_posts,
            'form': form,
        }
        return render(request, 'base.html', context)


class AboutView(View):
    """View with information about firm"""

    def get(self, request, *args, **kwargs):
        form = QuestionForm()
        context = {
            'form': form
        }
        return render(request, 'about.html', context)


class ContactView(View):
    """View with contact information"""

    def get(self, request, *args, **kwargs):
        form = QuestionForm()
        context = {
            'form': form
        }
        return render(request, 'contact.html', context)

    def post(self, request, *args, **kwargs):
        bound_form = QuestionForm(request.POST)
        if bound_form.is_valid():
            new_question = bound_form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Мы получили ваше сообщение. Ожидайте, мы скоро с вами свяжемся')
            return HttpResponseRedirect('/контакты')
        context = {
            'form': bound_form,
        }
        return render(request, 'contact.html', context)


class PostListView(ListView):
    """View with all posts"""
    model = Post
    context_object_name = 'posts'
    template_name = 'post_list.html'
    form = QuestionForm()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        return context
