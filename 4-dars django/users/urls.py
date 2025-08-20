from django.urls import path
from users.views import RegisterView,LoginView
from django.urls import path
app_name = 'users'

urlpatterns = [
    path('hisobga_kirish/',LoginView.as_view(), name='login'),
    path('royxatdan_otish/', RegisterView.as_view(), name='register' )

    
]