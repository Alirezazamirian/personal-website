from django import forms


class ContactMeForm(forms.Form):
    subject = forms.CharField(max_length=100, required=True, min_length=4, widget=forms.TextInput(
        attrs={'type': 'text', 'name': 'subject', 'id': 'subject', 'placeholder': "Your Subject *"}
    ),
                              error_messages={
                                  'required': 'this field is required!',
                                  'max_length': 'maximum length is 100 characters!',
                                  'min_length': 'minimum length is 4 characters!'
                              })
    email = forms.EmailField(max_length=100, required=True, min_length=10, widget=forms.TextInput(
        attrs={'type': 'email', 'name': 'email', 'id': 'email', 'placeholder': "Email *"}
    ), error_messages={
        'required': 'this field is required!',
        'max_length': 'maximum length is 100 characters!',
        'min_length': 'minimum length is 10 characters!'
    })
    name = forms.CharField(max_length=50, min_length=6, required=True, widget=forms.TextInput(
        attrs={'type': 'text', 'name': 'full-name', 'id': 'full-name', 'placeholder': "Name *"}
    ), error_messages={
        'required': 'this field is required!',
        'max_length': 'maximum length is 100 characters!',
        'min_length': 'minimum length is 6 characters!'
    })
    message = forms.CharField(max_length=300, min_length=10, required=True, widget=forms.Textarea(
        attrs={'name': 'message', 'id': 'message', 'placeholder': "Your Message *"}
    ), error_messages={
        'required': 'this field is required!',
        'max_length': 'maximum length is 300 characters!',
        'min_length': 'minimum length is 10 characters!'
    })
