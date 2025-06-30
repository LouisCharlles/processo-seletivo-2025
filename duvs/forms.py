from django import forms
from duvs.models import DUV, Passageiro, Navio

class DuvForm(forms.ModelForm):
    class Meta:
        model = DUV
        fields = ("data_viagem", "navio")

class NavioForm(forms.ModelForm):
    class Meta:
        model = Navio
        fields = ("nome", "bandeira", "imagem")

class PassageiroForm(forms.ModelForm):
    class Meta:
        model = Passageiro
        fields = ("duv", "nome", "tipo", "nacionalidade", "foto", "sid")
