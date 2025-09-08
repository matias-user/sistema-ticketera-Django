from django.shortcuts import render
from django.views.generic import DetailView

from users.models import Profile

# Create your views here.
class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'users/profile.html'
