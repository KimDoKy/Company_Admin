from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .models import CustomUser
from .forms import CustomUserCreationForm

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def profile(request):
    username = request.user.get_username()
    user = CustomUser.objects.get(custom_username=username)
    return render(request, 'profile.html', {'user':user})
