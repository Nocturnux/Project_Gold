from . import views
from django.urls import path

urlpatterns = [      
    path('', views.cabin_type, name='cabin_type'),   
    path('cabin_type_status_/<int:cabin_type_id>/', views.change_status_cabin_type, name='cabin_type_status'),         
]