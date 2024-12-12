from django import forms

from Petstagram.pets.models import Pets


class PetsBaseForm(forms.ModelForm):
    class Meta:
        model = Pets
        fields = ['name', 'date_of_birth', 'personal_photo']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Pet name'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'Date'}),
            'personal_photo': forms.Textarea(attrs={'placeholder': 'Link to image'}),
        }

        labels = {
            'name': 'Pet Name',
            'date_of_birth': 'Date of Birth',
            'personal_photo': 'Link to Image',
        }


class PetForm(PetsBaseForm):
    pass


class PetEditForm(PetsBaseForm):
    pass


class PetDeleteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values:
            field.disabled = True
            field.read_only = True
