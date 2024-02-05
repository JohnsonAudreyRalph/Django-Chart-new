from django.urls import path
from .views import *
 
urlpatterns = [
	path('', index, name='index'),
    path('get_data_day/', get_data_day, name='get_data_day'),
    path('char', char)
]