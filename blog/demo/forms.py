from django import forms
from django.core import validators
def gmail_ver(value):
    if value[len(value)-9:]!="gmail.com":
        raise  forms.ValidationError("this is not  a gmail account")
class feedbackform(forms.Form):
    name=forms.CharField()
    rollno=forms.IntegerField()
    email=forms.EmailField(validators=[gmail_ver])
    feed=forms.CharField(widget=forms.Textarea)
