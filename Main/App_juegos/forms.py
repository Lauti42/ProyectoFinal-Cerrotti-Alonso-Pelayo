
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
            'contenido',
        ]
        labels = {
            'nombre': 'Nombre',
            'anodecreacion': 'Año de creación',
            'desarrollador': 'Desarrollador',
            'genero': 'Género',
            'plataforma': 'Plataforma',
            'urlimagen': 'URL de la imagen',
            'descripcion': 'Descripción',
            'contenido': 'contenido',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'anodecreacion': forms.TextInput(attrs={'class':'form-control'}),
            'desarrollador': forms.TextInput(attrs={'class':'form-control',}),
            'genero': forms.TextInput(attrs={'class':'form-control'}),
            'plataforma':forms.TextInput(attrs={'class':'form-control',}),
            'urlimagen': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control','style':'height:250px;',}),
            'contenido': forms.Textarea(attrs={'class':'form-control','style':'height:250px;',}),
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

