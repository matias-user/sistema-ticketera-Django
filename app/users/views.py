from django.shortcuts import render
from django.views.generic import DetailView

from users.models import Profile
from ticket.models import Ticket

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