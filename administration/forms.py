from django import forms

from blog.models import Post
from question.models import Question


class PostForm(forms.ModelForm):
    """Model post form, if image uploaded"""

    class Meta:
        model = Post
        fields = ['title', 'short_description', 'image', 'is_on_main_page']


class PostWithoutImageForm(forms.ModelForm):
    """Model post form, if image don`t changed"""

    class Meta:
        model = Post
        fields = ['title', 'short_description', 'is_on_main_page']
