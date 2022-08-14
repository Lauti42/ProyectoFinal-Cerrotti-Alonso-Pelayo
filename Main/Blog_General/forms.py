from socket import fromshare
from django import forms
from .models import Entry, Comentario
from django.db import models

class NewCommentForm(forms.ModelForm):
    class Meta:
        model= Comentario
        fields= ("body",)
        widgets= {
            'body': forms.TextInput(
                attrs={
                    'placeholder': 'Comenta aqui'
                }
            )
        }
        
        