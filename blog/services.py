from blog.models import Post


def get_posts_for_main_page():
    """Returns posts to be displayed on the main page"""
    posts_for_main_page = Post.objects.filter(is_on_main_page=True)
    print(posts_for_main_page)
    return posts_for_main_page