from django import forms

# class ContactForm(forms.Form):
#     name= forms.CharField(max_length=50, label="Name")
#     email= forms.EmailField(max_length=50, label="Email")
#     message= forms.CharField(label='Message',widget=forms.Textarea(
#                         attrs={'placeholder': 'Enter your message here'}))
class ContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    message = forms.CharField(
        max_length=1000,
        widget=forms.Textarea(),
    )
    source = forms.CharField(       # A hidden input for internal use
        max_length=50,              # tell from which page the user sent the message
        widget=forms.HiddenInput()
    )

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')
        if not name and not email and not message:
            raise forms.ValidationError('You have to write something!')