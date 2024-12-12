from django import forms
from django.contrib.auth.models import User

from ExamPrepOne.album import choices
from ExamPrepOne.album.models import Album


class BaseForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

        album_name = forms.CharField(
            widget=forms.TextInput(attrs={
                'id': 'album_name',
                'placeholder': 'Album Name',
                'type': 'text',
            }),
        )

        artist = forms.CharField(
            widget=forms.TextInput(attrs={
                'id': 'artist',
                'placeholder': 'Artist',
                'type': 'text',
            })
        )

        genre = forms.ChoiceField(
            choices=Album.MUSIC_CHOICES,
            widget=forms.Select(attrs={
                'id': 'genre',
                'placeholder': 'Genre',
            })
        )

        description = forms.CharField(
            widget=forms.Textarea(attrs={
                'id': 'description',
                'placeholder': 'Description',
            })
        )

        image_url = forms.ImageField(
            widget=forms.TextInput(attrs={
                'id': 'image_url',
                'placeholder': 'Image URL',
                'type': 'url',
            })
        )

        price = forms.FloatField(
            widget=forms.NumberInput(attrs={
                'id': 'price',
                'placeholder': 'Price',
                'type': 'number',
            }),
        )


class CreateAlbumForm(BaseForm):
    pass


class EditAlbumForm(BaseForm):
    pass


class DeleteAlbumForm(BaseForm):
    pass
