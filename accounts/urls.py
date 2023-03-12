from django.urls import path , include
from accounts.views import *

urlpatterns = [
    path('login/', login_page, name='login_page'),
    path('register/', register_page, name='register_page'),
    path('login_signup/', login_signup_page, name='login_signup_page'),
    
    path('dashboard/',dashboard, name='dashboard'),
    path('user_management/',user_management, name='user_management'),
    path('tour_management/',tour_management, name='tour_management'),
    path('hotel_management/',hotel_management, name='hotel_management'),
    path('transport_management/',transport_management, name='tour_management_page'),
    path('add_package/',add_package, name='tour_management_page'),
    path('add_transport/',add_transport, name='tour_management_page'),
    path('add_hotel/',add_hotel, name='tour_management_page'),
    path('edit_package/<id>',edit_package, name='edit_package'),
    path('edit_hotel/<id>',edit_hotel, name='edit_hotel'),
    path('edit_transport/<id>',edit_transport, name='edit_transport'),
    path('delete_user/<email>',delete_user, name='delete_user'),
    path('delete_package/<id>',delete_package, name='delete_package'),
    path('delete_hotel/<id>',delete_hotel, name='delete_hotel'),
    path('delete_transport/<id>',delete_transport, name='delete_transport'),
         
    path('delete_image/<item>/<item_id>/<image_id>', delete_image, name='delete_image'), 
    path('status_update/<item>/<id>', status_update, name='status_update'), 
    path('image/',image, name='tour_management_page'),

]