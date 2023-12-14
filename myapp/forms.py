from django import forms
from .models import Colis

class ColisForm(forms.ModelForm):
    class Meta:
        model = Colis
        fields = [
            'LieuDepart',
            'LieuLivraison',
            'DateLivraison',
            'DescriptionColis',
        ]

        widgets = {
            'DateLivraison': forms.DateInput(attrs={'type': 'date'}),
        }