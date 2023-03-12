from django.urls import path , include
from packages.views import *

urlpatterns = [
    path('<slug>/', get_package, name='get_package'),
    path('transport/<slug>/', get_transport, name='get_transport'),
    path('hotel/<slug>/', get_hotel, name='get_hotel'),

]