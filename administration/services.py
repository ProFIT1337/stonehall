from question.services import get_qty_unanswered_feedback


def save_post_to_db(post, form):
    """Save changed post to db, with or without image"""
    post.title = form.cleaned_data['title']
    post.short_description = form.cleaned_data['short_description']
    post.is_on_main_page = form.cleaned_data['is_on_main_page']
    post.content = form.cleaned_data['content']
    if 'image' in form.cleaned_data:
        post.image = form.cleaned_data['image']
    post.save()


def add_feedback_qty_badge_to_context(context):
    """Supplements the passed context with information about the number of unanswered questions and returns it"""
    unanswered_feedback_qty = get_qty_unanswered_feedback()
    new_context = context.copy()
    new_context['unanswered_feedback_qty'] = unanswered_feedback_qty
    return new_context
