from . import views
from django.urls import path, include

urlpatterns = [
	path('show_employee', views.show_employee, name='show_employee'),
	path('get_data', views.get_data, name='get_data'),
]
