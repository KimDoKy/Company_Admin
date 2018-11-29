from django.urls import path
from django.views.generic import TemplateView 
from .views import SignUp, profile

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('', profile, name='profile'),
    ]
