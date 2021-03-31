from django.contrib import messages
from django.contrib.auth import authenticate, login

from blog.models import Post, PostImage
from mail.services import send_notification_about_feedback


def get_posts_for_main_page():
    """Returns six posts to be displayed on the main page"""
    posts_for_main_page = Post.objects.filter(is_on_main_page=True)
    return posts_for_main_page[:6]


def get_all_posts():
    """Returns all posts. Ordered by created date"""
    posts = Post.objects.all()
    return posts


def get_post_with_pk(pk: int):
    """Returns post with pk"""
    post = Post.objects.get(pk=pk)
    return post


def get_all_images():
    """Returns all images from model PostImage"""
    images = PostImage.objects.all()
    return images


def get_image_with_pk(pk: int):
    """Returns image with pk"""
    image = PostImage.objects.get(pk=pk)
    return image


def save_question_to_db(request, bound_form):
    """Save new question to db, and send notification email"""
    new_question = bound_form.save()
    messages.add_message(request, messages.SUCCESS,
                         'Мы получили ваше сообщение. Ожидайте, мы скоро с вами свяжемся')
    send_notification_about_feedback(new_question)


def login_user_to_site(request, form):
    """Login user to site, when returns True, else False"""
    username = form.cleaned_data['username']
    password = form.cleaned_data['password']
    user = authenticate(username=username, password=password)
    if user:
        login(request, user)
        return True
    return False
