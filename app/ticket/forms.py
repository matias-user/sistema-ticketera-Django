from django import forms
from .models import Ticket

from common.forms import BootstraClassespMixin

class TicketCreationForm(BootstraClassespMixin, forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title','description','assigned_to','department','categories','priority','state']
        widgets = {
            'description': forms.Textarea()
        }