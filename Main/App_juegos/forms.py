
from django import forms
from .models import ComentarioG, Juegos

class CreaJuegos(forms.ModelForm):

    class Meta:
        model = Juegos

        fields = [
            'nombre',
            'anodecreacion',
            'desarrollador',
            'genero',
            'plataforma',
            'urlimagen',
            'descripcion',
        ]
        labels = {
            'nombre': 'Nombre',
            'anodecreacion': 'Año de creación',
            'desarrollador': 'Desarrollador',
            'genero': 'Género',
            'plataforma': 'Plataforma',
            'urlimagen': 'URL de la imagen',
            'descripcion': 'Descripción',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'anodecreacion': forms.TextInput(attrs={'class':'form-control'}),
            'desarrollador': forms.Select(attrs={'class':'form-control', 'default': 'Elija el desarrollador'}),
            'genero': forms.Select(attrs={'class':'form-control'}),
            'plataforma': forms.Select(attrs={'class':'form-control'}),
            'urlimagen': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Imagen de 400x200'}),
            'descripcion': forms.Textarea(attrs={'rows': 5}),
        }
class NewCommentFormG(forms.ModelForm):
    class Meta:
        model= ComentarioG
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

