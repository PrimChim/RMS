from django.urls import path
from .views import *

app_name = 'users'
urlpatterns = [
    path('login/', login_view,name='logi'),
    path('',dashboard,name='dashboard'),
]
