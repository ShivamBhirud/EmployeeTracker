from django.contrib import admin
from django.urls import path
from employee import views
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/', include('employee.urls')),
	path('', views.home, name='home'),
]
