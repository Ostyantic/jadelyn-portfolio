from django.urls import path

from.views import HomePageView, PortfolioPageView, contact_page_view


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('portfolio/', PortfolioPageView.as_view(), name='portfolio'),
    path('contact/', contact_page_view, name='contact'),
]
