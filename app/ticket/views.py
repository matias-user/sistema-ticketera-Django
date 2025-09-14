from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from ticket.models import Ticket
from .forms import TicketCreationForm

# Create your views here.
class TicketListView(ListView):
    model = Ticket
    context_object_name = "tickets"
    template_name = "ticket/list_tickets.html"

class TicketDetailView(DetailView):
    model = Ticket
    context_object_name = "ticket"
    template_name = "ticket/detail_ticket.html"

class TicketCreateView(CreateView):
    model = Ticket
    template_name = 'ticket/create_ticket.html'
    form_class = TicketCreationForm
    success_url = reverse_lazy('ticket:list_tickets')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
