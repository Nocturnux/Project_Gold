from . import views
from django.urls import path

urlpatterns = [      
    path('', views.payment, name='payment'),
    path('payment_status_/<int:payment_id>/', views.change_status_payment, name='payment_status'),         
]