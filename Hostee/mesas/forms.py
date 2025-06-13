from django import forms
from .models import Mesa

class MesaForm(forms.ModelForm):
    class Meta:
        model = Mesa
        fields = ['numero', 'capacidad', 'estado']
        widgets = {
            'numero': forms.NumberInput(attrs={'class': 'form-control'}),
            'capacidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}, choices=Mesa.ESTADOS),
        }
