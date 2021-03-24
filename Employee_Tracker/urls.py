from django.contrib import admin
from django.urls import path
from employee import views
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/', include('employee.urls')),
	path('', views.home, name='home'),
]
