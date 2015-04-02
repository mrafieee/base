# from django.utils.translation import ugettext_lazy as _
# from django.core.exceptions import ObjectDoesNotExist
# from django.forms.util import ErrorList
# from django.forms import ModelForm
# from django import forms
# from models import Member,Article
#
# class RegisterForm(ModelForm):
# 	class Meta:
# 		model = Member
# 		exclude  = ('congress','code','status')
# 	def clean(self):
# 		cleaned_data = self.cleaned_data
# 		receipt = cleaned_data.get('receipt')
# 		try:
# 			receipt = Member.objects.get(receipt=receipt)
# 			self._errors['receipt'] = ErrorList([_('This receipt no. has already been registered')])
# 			del cleaned_data['receipt']
# 		except ObjectDoesNotExist:
# 			pass
# 		return cleaned_data
#
# class ConfirmForm(forms.Form):
# 	code = forms.CharField(_('Tracking Code'),help_text = _('Enter your registration tracking code in order to check your status.'), required = True)
# 	def clean(self):
# 		cleaned_data = self.cleaned_data
# 		code = cleaned_data.get('code')
# 		try:
# 			code = Member.objects.get(code=code)
# 			pass
# 		except ObjectDoesNotExist:
# 			self._errors['code'] = ErrorList([_('This tracking code no. is not available')])
# 			del cleaned_data['code']
# 		return cleaned_data
#
# class ArticleForm(ModelForm):
# 	class Meta:
# 		model = Article
# 		exclude  = ('congress','code','status','attachment')
# 	def clean(self):
# 		cleaned_data = self.cleaned_data
# 		return cleaned_data
#
# class ArticleConfirmForm(forms.Form):
# 	code = forms.CharField(_('Tracking Code'),help_text = _('Enter your Submission tracking code in order to check your status.'), required = True)
# 	def clean(self):
# 		cleaned_data = self.cleaned_data
# 		code = cleaned_data.get('code')
# 		try:
# 			code = Article.objects.get(code=code)
# 			pass
# 		except ObjectDoesNotExist:
# 			self._errors['code'] = ErrorList([_('This article tracking code no. is not available')])
# 			del cleaned_data['code']
# 		return cleaned_data