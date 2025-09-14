from django.urls import path
from .views import ExportTicketView

app_name='report'

urlpatterns = [
    path('export/',ExportTicketView.as_view(), name='export_tickets')
]