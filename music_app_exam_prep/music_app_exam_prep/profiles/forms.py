from django import forms

from music_app_exam_prep.profiles.models import Profile


class ProfileCreationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username'})
    )

    email = forms.EmailField(widget=forms.TextInput(attrs={
        'placeholder': 'Email'
    }))

    age = forms.IntegerField(widget=forms.NumberInput(attrs={
        'placeholder': 'Age'
    }))


class ProfileDeletionForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
