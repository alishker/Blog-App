from django import forms
from blog.models import Post, Comment


class postForm(forms.ModelForm):
    class meta:
        model = Post
        fields = ("author", "title", "text")
        widget = {
            "title": forms.TextInput(attrs={"class": "textinputclass"}),
            "text": forms.Textarea(
                attrs={"class": "editable medium-editor-textarea postcontent"}
            ),
        }


class commentsForm(forms.ModelForm):
    class meta:
        model = Comment
        fields = ("author", "text")

        widget = {
            "author": forms.TextInput(attrs={"class": "textinputclass"}),
            "text": forms.Textarea(attrs={"class": "editable medium-editor-textarea"}),
        }
