def save_post_to_db(post, form):
    """Save changed post to db, with or without image"""
    post.title = form.cleaned_data['title']
    post.short_description = form.cleaned_data['short_description']
    post.is_on_main_page = form.cleaned_data['is_on_main_page']
    if 'image' in form.cleaned_data:
        post.image = form.cleaned_data['image']
    post.save()
