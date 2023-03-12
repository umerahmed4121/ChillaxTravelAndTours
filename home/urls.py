from django.urls import path , include
from home.views import *

urlpatterns = [
    path('', index, name='index'),
    path('logout', logout_user, name='logout'),
    # path('transports', transport_index, name='transport_index'),
    
    path('destinations', destination_index, name='destinations_index'),
    path('flights', flights_index, name='flights_index'),
    path('transports', cars_index, name='cars_index'),
    path('hotels', hotels_index, name='hotels_index'),
    path('order_confirmation/<item>/<id>', order_confirmation, name='order_confirmation'),
    
]
