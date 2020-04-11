from django import forms
from blog.models import Post, comments


class postForm():

    class meta():
        model = postForm
        fields = ('author', 'title', 'text')
        widget = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable-medium-textarea postcontent'})
        }


class commentsForm():

    class meta():
        model = postForm
        fields = ('author', 'text')

        widget = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable-medium-textarea'})
        }
