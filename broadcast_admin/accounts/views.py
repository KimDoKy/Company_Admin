from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from .models import CustomUser


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def profile(request):
    user = CustomUser.objects.get(pk=1)
    print(request)
    return render(request, 'profile.html', {'user':user})
