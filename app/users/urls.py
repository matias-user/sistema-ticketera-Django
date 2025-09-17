from django.urls import path
from users import views
from django.contrib.auth import views as auth_views
from .forms import CustomLoginForm

app_name = 'users'
urlpatterns = [
    path('profile/<int:pk>', views.ProfileDetailView.as_view(), name='profile'),
    path('', 
        auth_views.LoginView.as_view(
            template_name='users/login.html',
            authentication_form=CustomLoginForm       
        ), 
        name='login'
    ),
    path(
        'register/',
        views.CustomUserCreateView.as_view(),
        name='register'
    ),
    path(
        'password_reset/',
        auth_views.PasswordResetView.as_view(
            template_name='users/password_reset.html'
        ),
        name='password_reset'     
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='users/password_reset_confirm.html'
        ),
        name='password_reset_confirm'     
    )
]