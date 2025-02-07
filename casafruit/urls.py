from django.urls import path
from .views import register
from .views import login
from .views import views
from .views import dashboard
from .views import file_import


urlpatterns=[
    path('register/', register.userRegister, name='register'),
    path('login/',login.userLogin, name='login'),
    path('dashboard/',dashboard.dashboardPage, name='dashboard'),
    path('logout/',views.logoutRedirect, name='logout'),
    path('settings/',file_import.fileImport, name='settings'),
    path('process/',file_import.processFileZip, name='process'),
    path('homepage/',views.homepage, name='homepage'),
]