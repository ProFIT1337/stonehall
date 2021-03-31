from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from django.urls import reverse

from blog.forms import PostForm, PostWithoutImageForm, ImageForm, ImageWithoutImageForm
from administration.services import save_post_to_db, add_feedback_qty_badge_to_context, save_image_to_db, \
    save_question_is_answered_field_to_db
from blog.services import get_all_posts, get_post_with_pk, get_all_images, get_image_with_pk
from question.services import get_all_questions, get_question_with_pk


class AdministrationBaseView(LoginRequiredMixin, View):
    """Base view for administration page"""

    def get(self, request, *args, **kwargs):
        context = {}
        context = add_feedback_qty_badge_to_context(context)
        return render(request, 'administration_base.html', context)


class NewPostView(LoginRequiredMixin, View):
    """Administration view with adding new post"""

    def get(self, request, *args, **kwargs):
        form = PostForm(request.POST or None, request.FILES or None)
        context = {'form': form}
        context = add_feedback_qty_badge_to_context(context)
        return render(request, 'administration_new_post.html', context)

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Пост создан')
            return HttpResponseRedirect(reverse('administration_base'))
        context = {'form': form}
        context = add_feedback_qty_badge_to_context(context)
        return render(request, 'administration_new_post.html', context)


class FeedbackView(LoginRequiredMixin, View):
    """Administration view with feedback information"""

    def get(self, request, *args, **kwargs):
        questions = get_all_questions()
        context = {
            'questions': questions
        }
        context = add_feedback_qty_badge_to_context(context)
        return render(request, 'administration_feedback.html', context)


class FeedbackAnsweredView(LoginRequiredMixin, View):
    """Endpoint for administration feedback form. Changes the value of the field is_answered?"""

    def post(self, request, *args, **kwargs):
        question_pk = kwargs.get('pk')
        is_answered = bool(request.POST.get('is_answered'))
        save_question_is_answered_field_to_db(request, question_pk, is_answered)
        return HttpResponseRedirect(reverse('administration_feedback'))


class FeedbackDeleteView(LoginRequiredMixin, View):
    """Endpoint for administration feedback form. Delete feedback"""

    def post(self, request, *args, **kwargs):
        question_pk = kwargs.get('pk')
        question = get_question_with_pk(question_pk)
        question.delete()
        messages.add_message(request, messages.SUCCESS, 'Фидбек удалён')
        return HttpResponseRedirect(reverse('administration_feedback'))


class EditPostView(LoginRequiredMixin, View):
    """Display all posts. The user can choose which post to change"""

    def get(self, request, *args, **kwargs):
        posts = get_all_posts()
        context = {
            'posts': posts
        }
        context = add_feedback_qty_badge_to_context(context)
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
        context = add_feedback_qty_badge_to_context(context)
        return render(request, 'administration_edit_specific_post.html', context)

    def post(self, request, *args, **kwargs):
        post = get_post_with_pk(kwargs.get('pk'))
        form_with_image = PostForm(request.POST or None, request.FILES or None)
        form_without_image = PostWithoutImageForm(request.POST)

        if form_with_image.is_valid():
            save_post_to_db(request, post, form_with_image)
            return HttpResponseRedirect(reverse('administration_base'))

        if form_without_image.is_valid():
            save_post_to_db(request, post, form_with_image)
            return HttpResponseRedirect(reverse('administration_base'))

        context = {
            'form': form_with_image,
            'post': post
        }
        context = add_feedback_qty_badge_to_context(context)
        return render(request, 'administration_edit_specific_post.html', context)


class DeletePostView(LoginRequiredMixin, View):
    """Display all posts. The user can choose which post to delete"""

    def get(self, request, *args, **kwargs):
        posts = get_all_posts()
        context = {
            'posts': posts
        }
        context = add_feedback_qty_badge_to_context(context)
        return render(request, 'administration_display_all_posts_to_delete.html', context)


class DeleteSpecificPostView(LoginRequiredMixin, View):
    """Endpoint to delete specific post"""

    def post(self, request, *args, **kwargs):
        post = get_post_with_pk(kwargs.get('pk'))
        post.delete()
        messages.add_message(request, messages.SUCCESS, 'Пост успешно удалён')
        return HttpResponseRedirect(reverse('administration_base'))


class ImagesListView(LoginRequiredMixin, View):
    """View with all images list"""

    def get(self, request, *args, **kwargs):
        images = get_all_images()
        context = {
            'images': images
        }
        context = add_feedback_qty_badge_to_context(context)
        return render(request, 'administration_display_all_images.html', context)


class NewImageView(LoginRequiredMixin, View):
    """Administration view with adding new image"""

    def get(self, request, *args, **kwargs):
        form = ImageForm(request.POST or None, request.FILES or None)
        context = {'form': form}
        context = add_feedback_qty_badge_to_context(context)
        return render(request, 'administration_new_image.html', context)

    def post(self, request, *args, **kwargs):
        form = ImageForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Фотография добавлена')
            return HttpResponseRedirect(reverse('administration_base'))
        context = {'form': form}
        context = add_feedback_qty_badge_to_context(context)
        return render(request, 'administration_new_image.html', context)


class ImageEditView(LoginRequiredMixin, View):
    """Changing a specific image on the administration page"""

    def get(self, request, *args, **kwargs):
        image = get_image_with_pk(kwargs.get('pk'))
        form = ImageForm(instance=image)
        context = {
            'form': form,
            'image': image
        }
        context = add_feedback_qty_badge_to_context(context)
        return render(request, 'administration_edit_specific_image.html', context)

    def post(self, request, *args, **kwargs):
        image = get_image_with_pk(kwargs.get('pk'))
        form_with_image = ImageForm(request.POST or None, request.FILES or None)
        form_without_image = ImageWithoutImageForm(request.POST)

        if form_with_image.is_valid():
            save_image_to_db(request, image, form_with_image)
            return HttpResponseRedirect(reverse('administration_base'))
        if form_without_image.is_valid():
            save_image_to_db(request, image, form_without_image)
            return HttpResponseRedirect(reverse('administration_base'))

        context = {
            'form': form_with_image,
            'image': image
        }
        context = add_feedback_qty_badge_to_context(context)
        return render(request, 'administration_edit_specific_image.html', context)


class ImageDeleteView(LoginRequiredMixin, View):
    """Endpoint to delete specific image"""

    def post(self, request, *args, **kwargs):
        image = get_image_with_pk(kwargs.get('pk'))
        image.delete()
        messages.add_message(request, messages.SUCCESS, 'Изображение успешно удалено')
        return HttpResponseRedirect(reverse('administration_base'))


class ChangeSerialNumber(LoginRequiredMixin, View):
    """Endpoint to change serial number of post"""

    def post(self, request, *args, **kwargs):
        post = get_post_with_pk(kwargs.get('pk'))
        post.serial_number = request.POST.get('serial_number')
        post.save()
        return HttpResponseRedirect(reverse('administration_edit_post'))


def clear_cache(request):
    """Clears the cache to update data from the database"""
    cache.clear()
    messages.add_message(request, messages.SUCCESS, 'Данные успешно обновлены из базы')
    return HttpResponseRedirect(reverse('administration_base'))
