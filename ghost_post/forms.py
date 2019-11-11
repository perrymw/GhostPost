from django import forms
from ghost_post.models import BoastandRoast

class PostForm(forms.ModelForm):
    class Meta:
        model = BoastandRoast
        fields = [
            'boast',
            'content'
        ]