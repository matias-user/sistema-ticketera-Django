from django.urls import path
from users import views
from django.contrib.auth import views as auth_views
from .forms import CustomLoginForm

app_name = 'users'
urlpatterns = [
    path('profile/<int:pk>', views.ProfileDetailView.as_view(), name='profile'),
    path(
        'login/', 
        auth_views.LoginView.as_view(
            template_name='users/login.html',
            authentication_form=CustomLoginForm       
        ), 
        name='login'),
]