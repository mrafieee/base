#encoding: utf-8
from django import forms
from django.utils.translation import ugettext_lazy as _


class ContactForm(forms.Form):
	name = forms.CharField(label=_('Full Name'))
	email = forms.EmailField(label=_('Email'), help_text=_('We will contact using this email address'))
	message = forms.CharField(label=_(), widget=forms.Textarea)
