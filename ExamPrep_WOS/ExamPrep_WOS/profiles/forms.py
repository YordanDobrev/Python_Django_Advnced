from django import forms

from ExamPrep_WOS.profiles.models import Profile


class ProfileCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Profile
        fields = [
            'username',
            'email',
            'age',
            'password'
        ]
        help_texts = {
            'age': 'Age requirement: 21 years and above.'
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
