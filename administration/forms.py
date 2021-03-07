from django import forms

from blog.models import Post
from question.models import Question


class NewPostForm(forms.ModelForm):
    """Form for creating new post"""

    class Meta:
        model = Post
        fields = ['title', 'short_description', 'image', 'is_on_main_page']


# class FeedbackForm(forms.Form):
#     """Feedback form in administration page"""
#
