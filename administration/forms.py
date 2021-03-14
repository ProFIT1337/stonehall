from django import forms

from blog.models import Post, PostImage

FIELDS_IN_POST_FORM = ['title', 'short_description', 'is_on_main_page', 'content']
FIELDS_IN_IMAGE_FORM = ['post']


class PostForm(forms.ModelForm):
    """Model post form, if image uploaded"""

    class Meta:
        model = Post
        fields = FIELDS_IN_POST_FORM[:]
        fields.append('image')


class PostWithoutImageForm(forms.ModelForm):
    """Model post form, if image don`t changed"""

    class Meta:
        model = Post
        fields = FIELDS_IN_POST_FORM[:]


class ImageForm(forms.ModelForm):
    """Model PostImage form, if image uploaded"""

    class Meta:
        model = PostImage
        fields = FIELDS_IN_IMAGE_FORM[:]
        fields.append('image')


class ImageWithoutImageForm(forms.ModelForm):
    """Model PostImage form, if image don`t changed"""

    class Meta:
        model = PostImage
        fields = FIELDS_IN_IMAGE_FORM[:]
