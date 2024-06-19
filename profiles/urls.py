from django.urls import path
from .views import *

urlpatterns = [
    path('', Index, name='index'),
    path('profile/', Profiles, name='profile'),
    path('view/', GetProfiles, name='view'),
]