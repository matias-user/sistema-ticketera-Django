from django.views.generic import ListView, DetailView

from ticket.models import Ticket

# Create your views here.
class TicketListView(ListView):
    model = Ticket
    context_object_name = "tickets"
    template_name = "ticket/list_tickets.html"

class TicketDetailView(DetailView):
    model = Ticket
    context_object_name = "ticket"
    template_name = "ticket/detail_ticket.html"