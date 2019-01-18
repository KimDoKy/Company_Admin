from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .models import CustomUser
from .forms import CustomUserCreationForm

from board.models import Board

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def profile(request):
    post_list = Board.objects.all()
    if request.user.is_authenticated:
        username = request.user.get_username()
        user = CustomUser.objects.get(custom_username=username)
        post_list = Board.objects.all()
        return render(request, 'home.html', {'user':user, 'post_list':post_list})
    else:
        return render(request, 'home.html', {'post_list':post_list})

