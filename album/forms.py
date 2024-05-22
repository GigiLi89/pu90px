from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {
            'body': 'Comment'
        }

class UserDeactivateForm(forms.Form):
    confirm = forms.BooleanField(label="Confirm deactivation")

class UserDeleteForm(forms.Form):
    confirm = forms.BooleanField(label="Confirm deletion")