from django.urls import path
from app1.views import home

app_name='app1'

urlpatterns = [
    path(route='',view=home,name='home'),
]
