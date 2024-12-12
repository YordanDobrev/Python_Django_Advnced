from django import forms

from Petstagram.common.models import Comment


class CommentForm(forms.Form):
    class Meta:
        model = Comment
        fields = ['text']

        widget = forms.Textarea(attrs={'placeholder': 'Add comment...'})
