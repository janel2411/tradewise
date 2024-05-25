from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name = "Sign Up")
    path('login', views.login, name = "Log In")
    path('signout', views.signout, name = "Sign Out")
]