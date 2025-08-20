from django.urls import path
from users.views import RegisterView,LoginView
from django.urls import path
from . import views


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register' ),
    path('login/',LoginView.as_view(), name='login'),
    path("login/", views.custom_login, name="login"),
]