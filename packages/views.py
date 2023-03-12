from django.shortcuts import render
from .models import *

# Create your views here.


    


def get_package(request, slug):

    try:
        package = Packages.objects.get(slug = slug)
        activites_inc = package.activites_inc.split(',')
        activites_not = package.activites_not.split(',')
        return render(request, 'packages/single_destination.html', context ={'package':package, 'activites_inc':activites_inc, 'activites_not':activites_not})
    except Exception as e:
        print(e)

def get_transport(request, slug):
    try:
        transport = Transport.objects.get(slug = slug)
        return render(request, 'packages/single_transport.html', context ={'transport':transport})
    except Exception as e:
        print(e)


def get_hotel(request, slug):
    try:
        
        hotel = Hotel.objects.get(slug = slug)
        facilities = hotel.facilities.split(',')
        return render(request, 'packages/single_hotel.html', context ={'hotel':hotel, 'facilities':facilities})
    except Exception as e:
        print(e)