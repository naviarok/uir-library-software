from django.urls import path
from .views import Home, Success, Error, HomeRedirect

urlpatterns = [
    path('home/', Home, name='home'),
    path('', HomeRedirect, name='homeRedirect'),
    path('success/', Success, name='success'),
    path('error/', Error, name='error'),
]