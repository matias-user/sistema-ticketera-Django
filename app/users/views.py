from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin 

from users.models import Profile

# Create your views here.
class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'users/profile.html'
    login_url = reverse_lazy('users:login')
