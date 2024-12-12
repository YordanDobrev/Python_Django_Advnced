from django import forms

from Artonia_v2.macrame.models import Macrame
from Artonia_v2.mixins import ReadOnlyMixin


class CreateMacrameForm(forms.ModelForm):
    class Meta:
        model = Macrame
        exclude = ['created_at', 'updated_at', 'user', 'is_public', 'bidder', 'last_bid']

    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Macrame name...'}))

    description = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Description...'
    }))

    price = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Price...'
    }))

    image_url = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Put Macrame URL...'
    }))

    knot_type = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Put a knot type...'}))

    bid_due_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
    )


class EditMacrameForm(CreateMacrameForm):
    pass


class EditMacrameBidForm(forms.ModelForm):
    class Meta:
        model = Macrame
        fields = ('last_bid',)

    last_bid = forms.DecimalField(widget=forms.TextInput(attrs={
        'placeholder': 'Place your best bid...'}),
        required=True
    )


class MacrameDeleteForm(ReadOnlyMixin, forms.ModelForm):
    class Meta:
        model = Macrame
        exclude = ['created_at', 'updated_at', 'user', 'is_public', 'bidder', 'last_bid']

    image_url = forms.CharField(
        label='Post Image URL:'
    )

    read_only_fields = ['name', 'description', 'price', 'image_url', 'knot_type', ]
