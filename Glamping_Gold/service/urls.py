from . import views
from django.urls import path

urlpatterns = [      
    path('', views.service, name='service'),
		path('service_status_/<int:service_id>/', views.change_status_service, name='service_status'),
    path('create/', views.create_service, name='create_service'),            
]