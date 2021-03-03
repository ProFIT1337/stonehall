from blog.models import Post


def get_posts_for_main_page():
    """Returns six posts to be displayed on the main page"""
    posts_for_main_page = Post.objects.filter(is_on_main_page=True)
    return posts_for_main_page[:6]