from django.views.generic import TemplateView
from django.core.mail import send_mail, EmailMessage
from port_project.settings import EMAIL_HOST_USER
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView
from .forms import ContactForm
from django.template.loader import render_to_string
# imported stuff for function
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse
from django.conf import settings


class HomePageView(TemplateView):
    template_name = 'home.html'


class PortfolioPageView(TemplateView):
    template_name = 'port.html'


def contact_page_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Get form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Construct email message
            email_subject = 'Portfolio contact submission'
            email_body = f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}'
            sender_email = email  # Your email here
            recipient_email = [settings.EMAIL_HOST_USER, ]  # List of recipient emails

            # Send email
            send_mail(email_subject, email_body, sender_email, recipient_email)

            return redirect(reverse('contact'))  # Redirect to success page
    else:
        form = ContactForm()

    return render(request, 'cont.html', {'form': form})
