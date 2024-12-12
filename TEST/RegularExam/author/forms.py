from django import forms

from RegularExam.author.models import Author


class AuthorCreateForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'passcode', 'pets_number']

    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Enter your first name...'
        }),
        label='First Name'
    )

    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Enter your last name...'
        }),
        label='Last Name'
    )

    passcode = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Enter 6 digits...',
        }),
        help_text='Your passcode must be a combination of 6 digits'
    )

    pets_number = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Enter the number of your pets...',
        }
    ),
        label='Pet Number'
    )


class AuthorUpdateForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'pets_number', 'info', 'image_url']

    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Enter your first name...'
        }),
        label='First Name'
    )

    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Enter your last name...'
        }),
        label='Last Name'
    )

    pets_number = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Enter the number of your pets...',
        }
    ),
        label='Pet Number'
    )

    image_url = forms.CharField(
        label='Profile Image URL:',
        required=False
    )
