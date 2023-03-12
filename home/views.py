from django.shortcuts import render,redirect
from packages.models import *
from django.contrib.auth import logout
import pandas as pd

class Flight():
    def __init__(self,code, airport, country) -> None:
        self.code = code
        self.airport = airport
        self.country = country
    

# Create your views here.
def index(request):
    no_of_items = 2
    some_pkgs = Packages.objects.all()[:no_of_items]
    some_htl = Hotel.objects.all()[:no_of_items]
    some_tpt = Transport.objects.all()[:no_of_items]

    if request.method == "GET":
        search = request.GET.get('search')
        if search != '' and search is not None:
            search_by = request.GET.get("search_by")
            if search_by == "package":
                return destination_index(request)
            elif search_by == "hotel":
                return hotels_index(request)
            elif search_by == "model":
                return cars_index(request)



    context = {'packages': some_pkgs, 'hotels':some_htl, 'transports':some_tpt}
    return render(request, 'home/home.html',context)

def transport_index(request):
    context = {'transports': Transport.objects.all()}
    return render(request, 'home/all_transport.html',context)

def destination_index(request):
    packages = Packages.objects.all()
    recent_trips = packages[:3]
    if packages:
        package1 = packages[0]
        countries = []
        min_price = int(package1.price)
        max_price = int(package1.price)
        for package in packages:
            price = int(package.price)
            if price < min_price:
                min_price = price
            if price > max_price:
                max_price = price
            if package.country not in countries:
                countries.append(package.country)
                

    if request.method == "GET":
        search = request.GET.get('search')
        if search != '' and search is not None:
            search_by = request.GET.get("search_by")
            if search_by == "package":
                packages = packages.filter(title__icontains=search)
            elif search_by == "location":
                packages = packages.filter(location__icontains=search)
            
        country = request.GET.get('country')
        price_range = request.GET.get('price_range')
        
        if country != "" and country is not None and price_range is not None: 
            price_range = int(price_range)
            if country != "all":
                packages = packages.filter(country__icontains=country)
            packages = packages.filter(price__lte=price_range)
    
    
    context = {'packages': packages,'recent_trips': recent_trips, 'countries': countries, "min_price": min_price, "max_price": max_price}
    return render(request, 'home/destination.html',context)

def flights_index(request):
    file_path = "home/airport_codes.xlsx"
    df = pd.read_excel(file_path)
    all_flights = []
    for i in range(len(df)):    
        flight = Flight(df.at[i,"Code"],df.at[i,"Airport"],df.at[i,"Country"])
        all_flights.append(flight)
    
    context = {"all_flights":all_flights}
    return render(request, 'home/transportation.html',context)

def cars_index(request):
    transports = Transport.objects.all()
    if transports:
        transport1 = transports[0]
        countries = []
        min_price = int(transport1.price)
        max_price = int(transport1.price)
        for transport in transports:
            price = int(transport.price)
            if price < min_price:
                min_price = price
            if price > max_price:
                max_price = price
            if transport.country not in countries:
                countries.append(transport.country)

    if request.method == "GET":
        search = request.GET.get('search')
        country = request.GET.get('country')
        price_range = request.GET.get('price_range')
        
        if search != "" and search is not None:
            search_by = request.GET.get("search_by")

            if search_by == "model":
                transports = transports.filter(model__icontains=search)
            elif search_by == "make":
                transports = transports.filter(make__icontains=search)
            
        if country != "" and country is not None and country != "all":
            transports = transports.filter(country__icontains=country)
            
        if price_range is not None:
            price_range = int(price_range)
            transports = transports.filter(price__lte=price_range)

            # change data type of price
    
    
    context = {'transports': transports, 'countries': countries, "min_price": min_price, "max_price": max_price}
    return render(request, 'home/car_transportation.html',context)

def hotels_index(request):
    hotels = Hotel.objects.all()
    recent_hotels = hotels[:3]
    if hotels:
        hotels1 = hotels[0]
        countries = []
        min_price = int(hotels1.price)
        max_price = int(hotels1.price)
        for hotel in hotels:
            price = int(hotel.price)
            if price < min_price:
                min_price = price
            if price > max_price:
                max_price = price
            if hotel.country not in countries:
                countries.append(hotel.country)

    if request.method == "GET":
        search = request.GET.get('search')
        if search != '' and search is not None:
            search_by = request.GET.get("search_by")
            if search_by == "hotel":
                hotels = hotels.filter(name__icontains=search)
            elif search_by == "location":
                hotels = hotels.filter(location__icontains=search)
            
        country = request.GET.get('country')
        price_range = request.GET.get('price_range')
        
        if country != "" and country is not None and price_range is not None: 
            price_range = int(price_range)
            if country != "all":
                hotels = hotels.filter(country__icontains=country)
            hotels = hotels.filter(price__lte=price_range)
    
    
    context = {'hotels': hotels,'recent_hotels': recent_hotels, 'countries': countries, "min_price": min_price, "max_price": max_price}
    return render(request, 'home/hotel.html',context)

def order_confirmation(request, item, id):

    if item == "package":
        obj = Packages.objects.get(uid = id)
        
    elif item == "hotel":
        obj = Hotel.objects.get(uid = id)
        
    elif item == "transport":
        obj = Transport.objects.get(uid = id)
        
    context = {"item_type":item,"item":obj}
    return render(request, 'home/order_confirmation.html',context)


def logout_user(request):
    logout(request)
    return redirect("/")

