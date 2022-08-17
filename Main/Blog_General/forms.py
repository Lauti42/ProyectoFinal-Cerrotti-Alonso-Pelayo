from socket import fromshare
from django import forms
from .models import Entry, Comentario
from django.db import models

class NewCommentForm(forms.ModelForm):
    class Meta:
        model= Comentario
        fields= ("body",)
        widgets= {
            'body': forms.Textarea(
                attrs={
                    'placeholder': 'Comenta aqui',
                    'width': 38,
                    'height': 100,
                    'cols': '115',
                    'rows': '3',
                    
                }
            )
        }
        
         