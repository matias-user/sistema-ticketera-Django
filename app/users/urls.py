from django.urls import path
from users import views

app_name = 'users'
urlpatterns = [
    path('profile/<int:pk>', views.ProfileDetailView.as_view(), name='profile')
]