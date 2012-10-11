from django import forms


class BlogForm(forms.Form):
    """docstring for BlogForm"""
    caption = forms.CharField(label='title', max_length=100)
    content = forms.CharField(widget=forms.Textarea)


class TagForm(forms.Form):
    """docstring for TagForm"""
    tag_name = forms.CharField()


class WeiboForm(forms.Form):
    """docstring for WeiboForm"""
    massage = forms.CharField(widget=forms.Textarea)
