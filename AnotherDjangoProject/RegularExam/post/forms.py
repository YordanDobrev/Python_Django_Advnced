from django import forms

from RegularExam.mixins import ReadOnlyMixin
from RegularExam.post.models import Post


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['updated_at', 'author']

    title = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Put an attractive and unique title...'
    }),
        error_messages={'unique': 'Oops! That title is already taken. How about something fresh and fun?'}
    )

    image_url = forms.CharField(
        help_text='Share your funniest furry photo URL!',
        label='Post Image URL:'
    )

    content = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Share some interesting facts about your adorable pets...'
    }))


class PostUpdateForm(PostCreateForm):
    image_url = forms.CharField(
        label='Post Image URL:'
    )


class PostDeleteForm(ReadOnlyMixin, forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['updated_at', 'author']

    image_url = forms.CharField(
        label='Post Image URL:'
    )

    read_only_fields = ['title', 'image_url', 'content']
