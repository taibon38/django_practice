from django.urls import path
from . import views

app_name = 'originalApps'
urlpatterns = [
    path('',views.index,name='index'),
]