from . import views
from django.urls import path

urlpatterns = [      
    path('', views.booking, name='booking'),
    path('booking_status_/<int:booking_id>/', views.change_status_booking, name='booking_status'),
    path('create/', views.create_booking, name='create_booking'),
    path('detail/<int:booking_id>/', views.detail_booking, name='detail_booking'),
    path('delete/<int:booking_id>/', views.delete_booking, name='delete_booking'),         
]