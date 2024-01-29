from . import views
from django.urls import path

urlpatterns = [      
    path('', views.booking, name='booking'),
    path('booking_status_/<int:booking_id>/', views.change_status_booking, name='booking_status'),         
]