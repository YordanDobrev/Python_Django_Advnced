from django import forms

from tasty_recypes.profiles.models import Profile


class ProfileCreationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'nickname',
            'first_name',
            'last_name',
            'chef'
        ]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'