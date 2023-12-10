from .models import Attraction
from django.forms import ModelForm, TextInput, Textarea, Select
from .models import Comment
from django import forms
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

class AttractionForms(ModelForm):
    class Meta:
        model = Attraction
        fields = ['attraction', 'attraction_type', 'region', 'information']

        widgets = {
            "attraction": TextInput(attrs={
                'class': 'alert alert-warning',
                'placeholder': 'Достопримечательность'
            }),
            "attraction_type": TextInput(attrs={
                'class': 'alert alert-warning',
                'placeholder': 'Тип достопримечательности'
            }),
            "region": TextInput(attrs={
                'class': 'alert alert-warning',
                'placeholder': 'Регион'
            }),
            "information": Textarea(attrs={
                'class': 'alert alert-warning',
                'placeholder': 'Информация'
            })
        }

class CommentForms(ModelForm):
    class Meta:
        model = Comment
        fields = ['user', 'subject', 'message', 'attraction']

        widgets = {
            "user": TextInput(attrs={
                'class': 'alert alert-warning',
                'placeholder': 'Пользователь'
            }),
            "subject": TextInput(attrs={
                'class': 'alert alert-warning',
                'placeholder': 'Тема'
            }),
            'message': Textarea(attrs={
                'class': 'alert alert-warning',
                'placeholder': 'Комментарий'
            }),
            'attraction': Select(attrs={
                'class': 'alert alert-warning',
                'placeholder': 'Достопримечательность'
            })
        }
