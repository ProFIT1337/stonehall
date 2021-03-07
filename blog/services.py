from blog.models import Post


def get_posts_for_main_page():
    """Returns six posts to be displayed on the main page"""
    posts_for_main_page = Post.objects.filter(is_on_main_page=True)
    return posts_for_main_page[:6]


def get_all_posts():
    """Returns all posts. Ordered by created date"""
    posts = Post.objects.order_by('-created_at')
    return posts


def get_post_with_pk(pk: int):
    """Returns post with pk"""
    post = Post.objects.get(pk=pk)
    return post
