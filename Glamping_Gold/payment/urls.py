from . import views
from django.urls import path

urlpatterns = [      
    path('', views.payment, name='payment'),
    path('payment_status_/<int:payment_id>/', views.change_status_payment, name='payment_status'),     
    path('create/', views.create_payment, name='create_payment'),    
    path('detail/<int:payment_id>/', views.detail_payment, name='detail_payment'),
    path('delete/<int:payment_id>/', views.delete_payment, name='delete_payment'),
    path('edit/<int:payment_id>/', views.edit_payment, name='edit_payment'), 
]