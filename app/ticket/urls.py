from django.urls import path
from ticket import views


app_name = 'ticket'
urlpatterns = [
    path('tickets/', views.TicketListView.as_view(), name='list_tickets' ),
    path('ticket/<int:pk>/', views.TicketDetailView.as_view(), name='detail_ticket' ),
]