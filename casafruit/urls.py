from django.urls import path
from .views import register
from .views import login
from .views import views

urlpatterns=[
    path('register/', register.userRegister, name='register'),
    path('login/',login.userLogin, name='login'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('logout/',views.logoutRedirect, name='logout'),
    path('homepage/',views.homepage, name='homepage'),
]