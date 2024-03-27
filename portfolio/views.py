from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView
from .forms import ContactForm
from django.template.loader import render_to_string


class HomePageView(TemplateView):
    template_name = 'home.html'


class PortfolioPageView(TemplateView):
    template_name = 'port.html'


class ContactPageView(FormView):
    template_name = 'cont.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        # Get form data
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']

        html = render_to_string('../templates/contact_form.html',
                                {
                                    'name': name,
                                    'email': email,
                                    'message': message,
                                })

        # Construct email message
        email_subject = 'Portfolio contact submission'
        email_body = f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}'
        sender_email = email  # Your email here
        # recipient_email = ['Jadelyn101@hotmail.com', ]  # List of recipient emails
        recipient_email = ['brendenm3603@gmail.com', ]  # List of recipient emails

        # Send email
        # email = EmailMessage(email_subject, email_body, sender_email, recipient_email)
        # email.send()
        send_mail(email_subject, email_body, sender_email, recipient_email, html_message=html)

        return super().form_valid(form)
