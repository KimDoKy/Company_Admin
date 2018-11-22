from django.urls import path
from django.views.generic import TemplateView 
from .views import SignUp, profile 

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html')),
    path('signup/', SignUp.as_view(), name='signup'),
    path('profile/', profile, name='profile'),
    ]
