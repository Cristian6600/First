
from django.urls import path

from . import views

app_name = "users_app"

urlpatterns = [
    
    path(
        '', 
        views.LoginUser.as_view(),
        name='user-login',
    ),

    path(
        'users/register/', 
        views.UserRegisterView.as_view(),
        name='user-register',
    ),

    path(
        'users/logout/', 
        views.LogoutView.as_view(),
        name='user-logout',
    ),

  
   
]
