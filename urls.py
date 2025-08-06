from django.urls import path
from . import views

urlpatterns = [

    path('', views.index_view, name='index'),
    path('login/', views.login_view, name='login'),
    path('customers/add/', views.add_customer, name='add_customer'),
    path('rides/', views.ride_list, name='ride_list'),
    path('rides/add/', views.add_ride, name='add_ride'),
    path('rides/edit/<int:ride_id>/', views.edit_ride, name='edit_ride'),
    path('rides/delete/<int:ride_id>/', views.delete_ride, name='delete_ride'),
   
]


