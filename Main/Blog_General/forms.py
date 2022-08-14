from socket import fromshare
from django import forms
from .models import Entry, Comentario

class NewCommentForm(forms.ModelForm):
    class Meta:
        model= Comentario
        fields= ("body",)
        