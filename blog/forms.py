from django import forms
from django.contrib.auth.models import User

from blog.models import Post, PostImage

FIELDS_IN_POST_FORM = ['title', 'short_description', 'is_on_main_page', 'content', 'image_y_offset', 'serial_number']
FIELDS_IN_IMAGE_FORM = ['post', 'description']


class PostForm(forms.ModelForm):
    """Model post form, if image uploaded"""

    def __init__(self, *args, **kwargs):
        """Add help_text to image_y_offset field"""
        super().__init__(*args, **kwargs)
        self.fields['image_y_offset'].help_text = "Смещение указывается в процентах. " \
                                                  " Имеет смысл только у вертикальных фотографий." \
                                                  " Указывается от 0 до 100, где 100 - самая нижняя точка"

    def clean_image_y_offset(self):
        data = self.cleaned_data['image_y_offset']
        if data < 0 or data > 100:
            raise forms.ValidationError("Значение должно быть от 0 до 100")
        return data

    class Meta:
        model = Post
        fields = FIELDS_IN_POST_FORM[:]
        fields.append('image')


class PostWithoutImageForm(forms.ModelForm):
    """Model post form, if image don`t changed"""

    def clean_image_y_offset(self):
        data = self.cleaned_data['image_y_offset']
        print(data)
        if data < 0 or data > 100:
            raise forms.ValidationError("Значение должно быть от 0 до 100")
        return data

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


class LoginForm(forms.ModelForm):
    """User login form"""
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        """Rename login form fields"""
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['username'].help_text = ''
        self.fields['password'].label = 'Пароль'
        self.fields['password'].help_text = ''

    def clean(self):
        """Username and password validation"""
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError(f'Пользователь с логином {username} не найден в системе.')
        user = User.objects.filter(username=username).first()
        if user:
            if not user.check_password(password):
                raise forms.ValidationError('Пароль введён неверно')
        return self.cleaned_data

    class Meta:
        model = User
        fields = ['username', 'password']
