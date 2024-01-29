from . import views
from django.urls import path

urlpatterns = [      
    path('', views.customer, name='customer'),
    path('customer_status_/<int:customer_id>/', views.change_status_customer, name='customer_status'),           
]