from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View

from administration.forms import PostForm, PostWithoutImageForm
from administration.services import save_post_to_db
from blog.services import get_all_posts, get_post_with_pk
from question.services import get_all_questions, get_question_with_pk


class AdministrationBaseView(LoginRequiredMixin, View):
    """Base view for administration page"""

    def get(self, request, *args, **kwargs):
        return render(request, 'administration_base.html', {})


class NewPostView(LoginRequiredMixin, View):
    """Administration view with adding new post"""

    def get(self, request, *args, **kwargs):
        form = PostForm(request.POST or None, request.FILES or None)
        context = {'form': form}
        return render(request, 'administration_new_post.html', context)

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST or None, request.FILES or None)
        context = {'form': form}
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Пост создан')
            return HttpResponseRedirect('/администрирование')
        return render(request, 'administration_new_post.html', context)


class FeedbackView(LoginRequiredMixin, View):
    """Administration view with feedback information"""

    def get(self, request, *args, **kwargs):
        questions = get_all_questions()
        context = {
            'questions': questions
        }
        return render(request, 'administration_feedback.html', context)


class FeedbackAnsweredView(LoginRequiredMixin, View):
    """Endpoint for administration feedback form. Changes the value of the field is_answered?"""

    def post(self, request, *args, **kwargs):
        question_pk = kwargs.get('pk')
        question = get_question_with_pk(question_pk)
        is_answered = bool(request.POST.get('is_answered'))
        question.is_answered = is_answered
        question.save()
        messages.add_message(request, messages.SUCCESS, 'Изменение сохранено')
        return HttpResponseRedirect('/администрирование/фидбек')


class EditPostView(LoginRequiredMixin, View):
    """Display all posts. The user can choose which post to change"""

    def get(self, request, *args, **kwargs):
        posts = get_all_posts()
        context = {
            'posts': posts
        }
        return render(request, 'administration_display_all_posts_to_edit.html', context)


class EditSpecificPostView(LoginRequiredMixin, View):
    """Changing a specific post on the administration page"""

    def get(self, request, *args, **kwargs):
        post = get_post_with_pk(kwargs.get('pk'))
        form = PostForm(instance=post)
        context = {
            'form': form,
            'post': post
        }
        return render(request, 'administration_edit_specific_post.html', context)

    def post(self, request, *args, **kwargs):
        post = get_post_with_pk(kwargs.get('pk'))
        form_with_image = PostForm(request.POST or None, request.FILES or None)
        form_without_image = PostWithoutImageForm(request.POST)

        if form_with_image.is_valid():
            save_post_to_db(post, form_with_image)
            messages.add_message(request, messages.SUCCESS, 'Пост успешно изменён')
            return HttpResponseRedirect('/администрирование/')

        if form_without_image.is_valid():
            save_post_to_db(post, form_with_image)
            messages.add_message(request, messages.SUCCESS, 'Пост успешно изменён')
            return HttpResponseRedirect('/администрирование/')

        context = {
            'form': form_with_image,
            'post': post
        }
        return render(request, 'administration_edit_specific_post.html', context)


class DeletePostView(LoginRequiredMixin, View):
    """Display all posts. The user can choose which post to delete"""

    def get(self, request, *args, **kwargs):
        posts = get_all_posts()
        context = {
            'posts': posts
        }
        return render(request, 'administration_display_all_posts_to_delete.html', context)


class DeleteSpecificPostView(LoginRequiredMixin, View):
    """Endpoint to delete specific post"""

    def post(self, request, *args, **kwargs):
        post = get_post_with_pk(kwargs.get('pk'))
        post.delete()
        return HttpResponseRedirect('/администрирование/')
