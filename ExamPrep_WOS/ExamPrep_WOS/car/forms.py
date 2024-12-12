from django import forms

from ExamPrep_WOS.car.models import Car
from ExamPrep_WOS.mixins import ReadOnlyMixin


class CarCreateForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ['owner']

    image_url = forms.URLField(
        widget=forms.TextInput(attrs={
            'placeholder': 'https://...'
        }))


class CarDetailForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ['owner']


class CarDeleteForm(ReadOnlyMixin, CarDetailForm):
    read_only_fields = ['type', 'model', 'year', 'image_url', 'price']

    image_url = forms.URLField(
        widget=forms.TextInput(attrs={
            'placeholder': ''
        })
    )
