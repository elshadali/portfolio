from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Message


class ContactForm(forms.ModelForm):
    mail = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': _('E-mail')
    }))
    subject = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': _('Subject')
    }))
    text = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': _('Text'),
        'rows': '6'
    }))

    class Meta:
        model = Message
        fields = ['mail', 'subject', 'text']