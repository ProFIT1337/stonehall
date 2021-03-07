from django import forms

from blog.models import Post


class NewPostForm(forms.ModelForm):
    """Form for creating new post"""

    class Meta:
        model = Post
        fields = ['title', 'short_description', 'image', 'is_on_main_page']

