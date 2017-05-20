from django import forms
 
from .models import Comment2
 
 
class Comment2Form(forms.Form):
 
    parent_comment = forms.IntegerField(
        widget=forms.HiddenInput,
        required=False
    )

    author = forms.CharField(
    	label="Автор",
    	widget=forms.TextInput
    )
 
    comment_area = forms.CharField(
        label="",
        widget=forms.Textarea
    )