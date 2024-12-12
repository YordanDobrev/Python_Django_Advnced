from django import forms
from django.forms import widgets

from ExamPrepOne.account.models import Profile


class BaseProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileCreationForm(BaseProfile):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'id': 'username',
            'placeholder': 'Username'
        })
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'id': 'email',
            'placeholder': 'Email'
        })
    )

    age = forms.IntegerField(
        min_value=0,
        widget=forms.NumberInput(attrs={
            'placeholder': 'Age'},
        ),
        required=False
    )


class ProfileUpdateForm(BaseProfile):
    pass


class ProfileDeleteForm(BaseProfile):
    pass
