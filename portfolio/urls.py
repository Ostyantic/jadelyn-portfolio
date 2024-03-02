from django.urls import path

from.views import HomePageView, PortfolioPageView, ContactPageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('portfolio/', PortfolioPageView.as_view(), name='portfolio'),
    path('contact/', ContactPageView.as_view(), name='contact'),
]
