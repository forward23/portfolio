from django.contrib import messages
from django.shortcuts import render
from django.views.generic import FormView
from .forms import ContactForm


class HomeView(FormView):
    template_name = 'index.html'
    form_class = ContactForm
    success_url = '/#contact'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        messages.success(self.request, 'Message has been sent!')
        return super().form_valid(form)