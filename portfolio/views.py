from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class PortfolioPageView(TemplateView):
    template_name = 'port.html'


class ContactPageView(TemplateView):
    template_name = 'cont.html'
