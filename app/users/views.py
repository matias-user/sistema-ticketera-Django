from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView

from users.models import CustomUser, Profile
from ticket.models import Ticket
from .forms import CustomUserCreationForm


# Create your views here.
class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'users/profile.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.get_object()
        context['tickets'] = Ticket.objects.filter(user=profile.user)
        return context
    
class CustomUserCreateView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

