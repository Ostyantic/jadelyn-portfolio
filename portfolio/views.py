from django.views.generic import TemplateView
from django.core.mail import send_mail
from port_project.settings import EMAIL_HOST_USER
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView
from .forms import ContactForm
# imported stuff for function
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse



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

            html = render_to_string('../templates/contact_form.html',
                                    {
                                        'name': name,
                                        'email': email,
                                        'message': message,
                                    })
            # Construct email message
            email_subject = 'New portfolio contact submission'
            email_body = f'{name} would like to connect with you!'
            sender_email = email  # Your email here
            recipient_email = [EMAIL_HOST_USER,]  # List of recipient emails

            # Send email
            send_mail(email_subject, email_body, sender_email, recipient_email, html_message=html)

            # return redirect(reverse('contact'))  # Redirect to success page
    else:
        form = ContactForm()

    return render(request, 'cont.html', {'form': form})
