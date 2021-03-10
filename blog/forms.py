from django import forms
from django.contrib.auth.models import User


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
