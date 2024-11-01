from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
<<<<<<< HEAD
        fields = ('title', 'text', 'image')
=======
        fields = ('title', 'text','image')
>>>>>>> 9e03a55796a976fc423e374eac8b7f1e44657d45
