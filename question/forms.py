from django import forms

from question.models import Question


class QuestionForm(forms.ModelForm):
    """Form for feedback"""

    class Meta:
        model = Question
        fields = ['sender_name', 'sender_contact_information', 'feedback_subject', 'feedback_text']
        widgets = {
            'sender_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше имя',
                'name': 'name',
                'id': 'name',
            }),
            'sender_contact_information': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Контактная информация',
                'name': 'contactInformation',
                'id': 'contactInformation'
            }),
            'feedback_subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тема',
                'name': 'subject',
                'id': 'subject'
            }),
            'feedback_text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Сообщение',
                'id': 'message',
                'cols': '30',
                'rows': 4
            }),
        }
