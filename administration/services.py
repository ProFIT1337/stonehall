from django.contrib import messages

from question.services import get_qty_unanswered_feedback, get_question_with_pk


def save_post_to_db(request, post, form):
    """Save changed post to db, with or without image"""
    post.title = form.cleaned_data['title']
    post.short_description = form.cleaned_data['short_description']
    post.is_on_main_page = form.cleaned_data['is_on_main_page']
    post.content = form.cleaned_data['content']
    post.serial_number = form.cleaned_data['serial_number']
    if 'image' in form.cleaned_data:
        post.image = form.cleaned_data['image']
    post.image_y_offset = form.cleaned_data['image_y_offset']
    post.save()
    messages.add_message(request, messages.SUCCESS, 'Пост успешно изменён')


def add_feedback_qty_badge_to_context(context):
    """Supplements the passed context with information about the number of unanswered questions and returns it"""
    unanswered_feedback_qty = get_qty_unanswered_feedback()
    new_context = context.copy()
    new_context['unanswered_feedback_qty'] = unanswered_feedback_qty
    return new_context


def save_image_to_db(request, image, form):
    """Save changed image to db, with or without changed image"""
    image.post = form.cleaned_data['post']
    image.description = form.cleaned_data['description']
    if 'image' in form.cleaned_data:
        image.image = form.cleaned_data['image']
    image.save()
    messages.add_message(request, messages.SUCCESS, 'Фотография успешно сохранена')

def save_question_is_answered_field_to_db(request, question_pk, is_answered):
    """Save question to db, when is_answered field was changed"""
    question = get_question_with_pk(question_pk)
    question.is_answered = is_answered
    question.save()
    messages.add_message(request, messages.SUCCESS, 'Изменение сохранено')

