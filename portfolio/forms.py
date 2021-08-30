from django import forms
from django.core.mail import send_mail


class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=25)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    full_name.widget.attrs.update({'id': 'name',
                                   'name': 'name',
                                   'placeholder': 'Full Name',
                                   'class': 'form-control px-0 mb-4'})

    email.widget.attrs.update({'id': 'email',
                                   'name': 'email',
                                   'placeholder': 'Email Address',
                                   'class': 'form-control px-0 mb-4'})

    message.widget.attrs.update({'id': 'message',
                                   'name': 'message',
                                   'placeholder': 'Type Message Here',
                                   'class': 'form-control px-0 mb-4'})

    def send_email(self):
        # send email using the self.cleaned_data dictionary

        send_mail(
            f"Message from {self.cleaned_data['full_name']}",
            self.cleaned_data['message'],
            self.cleaned_data['email'],
            ['ilia2307@gmail.com', ]
        )
