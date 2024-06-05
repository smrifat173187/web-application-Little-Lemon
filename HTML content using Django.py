from django.views.generic import TemplateView
from django.urls import path

class HomePageView(TemplateView):
    template_name = 'index.html'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]
