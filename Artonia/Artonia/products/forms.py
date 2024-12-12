from django import forms
from Artonia.products.models import Macrame, ArtPainting


class MacrameForm(forms.ModelForm):
    class Meta:
        model = Macrame
        fields = '__all__'


class ArtForm(forms.ModelForm):
    class Meta:
        model = ArtPainting
        fields = '__all__'

    name = forms.CharField(
        error_messages={
            "required": "Title is required",
        }
    )
