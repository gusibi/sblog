from django import forms


class ContactForm(forms.Form):
    """docstring for ContactForm"""
    subject = forms.CharField()
    email = forms.EmailField(required=False, label='Your e-mail address')
    message = forms.CharField(widget=forms.Textarea)

    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("Not enough words!")
        return message


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
