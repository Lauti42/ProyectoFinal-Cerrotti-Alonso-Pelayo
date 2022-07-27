from django import forms

class PreferenciasFormulario(forms.Form):

    lenguaje = forms.CharField()
    backofront = forms.CharField()
    pais = forms.CharField()
    trabajo = forms.CharField() 
    