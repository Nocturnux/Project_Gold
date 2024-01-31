from . import views
from django.urls import path

urlpatterns = [      
    path('', views.cabin, name='cabin'),
		path('cabin_status_/<int:cabin_id>/', views.change_status_cabin, name='cabin_status'),
    path('create/', views.create_cabin, name='create_cabin'),               
]