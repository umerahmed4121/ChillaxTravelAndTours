from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from packages.models import *
from .models import Image
from .forms import *
from datetime import datetime

from django.views.generic.edit import FormView


# class FileFieldFormView(FormView):
#     form_class = ImageForm
#     template_name = 'image.html'  # Replace with your template.
#     success_url = '/accounts/image'  # Replace with your URL or reverse().

#     def post(self, request, *args, **kwargs):
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         files = request.FILES.getlist('file_field')
#         if form.is_valid():
#             for f in files:
#                 PackagesImage(image=f)
                
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)


class Field:
    def __init__(self,field:str,value="",type="text") -> None:
        self.name = field
        split_field = field.split("_")
        strg = ""
        for i in split_field:
            strg += str.capitalize(i) + " "
        self.label = strg
        self.type = type
        self.placeholder = "Enter "+strg
        self.value = value

class Activity:
    def __init__(self, item, detail) -> None:
        self.item = item
        self.detail = detail

# Create your views here.

def dashboard(request):
    all_users = Profile.objects.all()
    all_pkgs = Packages.objects.all()
    all_htls = Hotel.objects.all()
    all_tpts = Transport.objects.all()
    no_of_users = len(all_users)
    no_of_pkgs = len(all_pkgs)
    no_of_htls = len(all_htls)
    no_of_tpts = len(all_tpts)

    last_up = all_pkgs[0]
    slast_up = all_pkgs[0]
    tlast_up = all_pkgs[0]
    last_cd = all_pkgs[0]
    slast_cd = all_pkgs[0]
    tlast_cd = all_pkgs[0]
    
    
    for item in all_pkgs:
        if item.updated_at > last_up.updated_at:
            tlast_up = slast_up
            slast_up = last_up
            last_up = item
        if item.created_at > last_cd.created_at:
            tlast_cd = slast_cd
            slast_cd = last_cd
            last_cd = item

    for item in all_htls:
        if item.updated_at > last_up.updated_at:
            tlast_up = slast_up
            slast_up = last_up
            last_up = item
        if item.created_at > last_cd.created_at:
            tlast_cd = slast_cd
            slast_cd = last_cd
            last_cd = item

    for item in all_pkgs:
        if item.updated_at > last_up.updated_at:
            tlast_up = slast_up
            slast_up = last_up
            last_up = item
        if item.created_at > last_cd.created_at:
            tlast_cd = slast_cd
            slast_cd = last_cd
            last_cd = item
    
    if request.method == "GET":
        search = request.GET.get("search")
        if search != "" and search is not None:
            all_pkgs = all_pkgs.filter(title__icontains=search)
            all_htls = all_htls.filter(name__icontains=search)
            all_tpts = all_tpts.filter(model__icontains=search)


    context ={
        "no_of_users" : no_of_users,
        "no_of_packages" : no_of_pkgs,
        "no_of_hotels" : no_of_htls,
        "no_of_transports" : no_of_tpts,
        "packages" : all_pkgs[:3],
        "hotels": all_htls[:3],
        "transports": all_tpts[:3],
        "last_up": last_up,
        "slast_up": slast_up,
        "tlast_up": tlast_up,
        "last_cd": last_cd,
        "slast_cd": slast_cd,
        "tlast_cd": tlast_cd,
        


    }
    return render(request, 'accounts/dashboard.html',context)


def tour_management(request):
    all_pkgs = Packages.objects.all()
    if request.method == "GET":
        search = request.GET.get("search")
        if search != "" and search is not None:
            all_pkgs = all_pkgs.filter(title__icontains=search)

    context = {'packages': all_pkgs}
    return render(request, 'accounts/tour_managment.html',context)

def hotel_management(request):
    all_pkgs = Hotel.objects.all()
    if request.method == "GET":
        search = request.GET.get("search")
        if search != "" and search is not None:
            all_pkgs = all_pkgs.filter(name__icontains=search)
           
    context = {'hotels': all_pkgs}
    return render(request, 'accounts/hotel_managment.html',context)

def transport_management(request):
    all_pkgs = Transport.objects.all()
    if request.method == "GET":
        search = request.GET.get("search")
        if search != "" and search is not None:
            all_pkgs = all_pkgs.filter(model__icontains=search)

    context = {'transports': all_pkgs}
    return render(request, 'accounts/transport_managment.html',context)

def user_management(request):
    all_users = Profile.objects.all()
    context = {'all_users': all_users}
    return render(request, 'accounts/user_management.html',context)

def delete_user(request, email):
    user = User.objects.get(email = email)
    user.delete()
    return redirect("/accounts/user_management")


def status_update(request,item , id):
    
    if item == "package":
        obj = Packages.objects.get(uid = id)
        page = "tour_management"
    elif item == "hotel":
        obj = Hotel.objects.get(uid = id)
        page = "hotel_management"
    elif item == "transport":
        obj = Transport.objects.get(uid = id)
        page = "transport_management"
    if obj.status == True:
        obj.status = False
    else:
        obj.status = True
    obj.save()
    return redirect('/accounts/'+page+'/')



def handle_uploaded_file(f,directory):
        with open('public/static/'+directory+'/' + f.name,'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)

def image(request):
    form = ImageForm()
    if request.method == "POST":
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            images = request.FILES.getlist('file_field')
            print(images)
            for image in images:

                handle_uploaded_file(image)
            return redirect("/accounts/image") 
        else:
            form = ImageForm()
            
    return render(request, "accounts/image.html",{"form":form})
        



def add_package(request):
    form = ImageForm()
    if request.method == "POST":
        title = request.POST.get('title')
        location = request.POST.get('location')
        country = request.POST.get('country')
        activites_inc = request.POST.get('activites_included')
        activites_not = request.POST.get('activites_not_included')
        duration = request.POST.get('duration')
        price = request.POST.get('price')
        details = request.POST.get('details')
    
        try:
            package = Packages.objects.get(slug = slugify(title))
            if package:
                messages.warning(request, 'This package already exist')
                return HttpResponseRedirect(request.path_info)

        except Exception as e:
            print(e)

        pkg = Packages(
            title = title,
            activites_inc = activites_inc,
            activites_not =activites_not,
            duration = duration,
            location = location,
            country = country,
            details = details,
            price = price,
            created_at = datetime.now(),
            updated_at = datetime.now(),
            
        )
        pkg.save()

        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            images = request.FILES.getlist('images')
            
            for image in images:
                handle_uploaded_file(image,"package")
                PackagesImage.objects.create(package = pkg,image =  "package/"+image.name,created_at = datetime.now(),
            updated_at = datetime.now(),)
        else:
            form = ImageForm()
            
            
        return redirect('/accounts/tour_management/')
    
    field_list =[
        Field("title"),
        Field("location"),
        Field("country"),
        Field("activites_included"),
        Field("activites_not_included"),
        Field("duration"),
        Field("price",type="number"),
        Field("details"),
    ]
    
    item = "package"
    all_items = ["package","hotel","transport"]
    context = {"form":form,"item":item,"all_items":all_items,"fields":field_list}
    return render(request, 'accounts/add_item.html', context)

def add_transport(request):
    form = ImageForm()
    if request.method == "POST":
        make = request.POST.get('make')
        model = request.POST.get('model')
        varient = request.POST.get('varient')
        color = request.POST.get('color')
        year = request.POST.get('year')
        country = request.POST.get('country')
        seating_capacity = request.POST.get('seating_capacity')
        price = request.POST.get('price')
        


        try:
            package = Packages.objects.get(slug = slugify(model))
            if package:
                messages.warning(request, 'This transport already exist')
                return HttpResponseRedirect(request.path_info)

        except Exception as e:
            print(e)

        tpt = Transport(
            make = make,
            model = model,
            varient = varient,
            color = color,
            year = year,
            country = country,
            seating_capacity = seating_capacity,
            price = price,
            created_at = datetime.now(),
            updated_at = datetime.now(),
        )
        tpt.save()
        
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            images = request.FILES.getlist('images')
            
            for image in images:
                handle_uploaded_file(image,"transport")
                TransportImage.objects.create(transport = tpt,image =  "transport/"+image.name,created_at = datetime.now(),
            updated_at = datetime.now(),)
        else:
            form = ImageForm()
            
            
        return redirect('/accounts/tour_management/')

    field_list =[
        Field("make"),
        Field("model"),
        Field("varient"),
        Field("color"),
        Field("year"),
        Field("country"),
        Field("seating_capacity"),
        Field("price"),
    ]
    item = "transport"
    all_items = ["package","hotel","transport"]
    context = {"form":form,"item":item,"all_items":all_items,"fields":field_list}
    return render(request, 'accounts/add_item.html', context)
    
def add_hotel(request):
    form = ImageForm()
    if request.method == "POST":
        name = request.POST.get('name')
        facilities = request.POST.get('facilities')
        location = request.POST.get('location')
        rooms = request.POST.get('rooms')
        country = request.POST.get('country')
        details = request.POST.get('details')
        price = request.POST.get('price')

        try:
            package = Packages.objects.get(slug = slugify(name))
            if package:
                messages.warning(request, 'This package already exist')
                return HttpResponseRedirect(request.path_info)

        except Exception as e:
            print(e)

        htl = Hotel(
            name = name,
            facilities = facilities,
            location = location,
            rooms = rooms,
            country = country,
            details = details,
            price = price,
            created_at = datetime.now(),
            updated_at = datetime.now(),
        )
        htl.save()
        
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            images = request.FILES.getlist('images')
            
            for image in images:
                handle_uploaded_file(image,"hotel")
                HotelImage.objects.create(hotel = htl,image =  "hotel/"+image.name,created_at = datetime.now(),
            updated_at = datetime.now(),)
        else:
            form = ImageForm()
            
        return redirect('/accounts/tour_management/')

    field_list =[
        Field("name"),
        Field("facilities"),
        Field("location"),
        Field("rooms"),
        Field("country"),
        Field("details"),
        Field("price"),
    ]
    item = "hotel"
    all_items = ["package","hotel","transport"]
    context = {"form":form,"item":item,"all_items":all_items,"fields":field_list}
    return render(request, 'accounts/add_item.html', context)
    
def edit_package(request, id):

    form = ImageForm()
    package = Packages.objects.get(uid = id)
    
    all_images = PackagesImage.objects.all()
    package_images = []
    for image in all_images:
        if image.package == package:
            package_images.append(image)
        

    if request.method == "POST":
        title = request.POST.get('title')
        location = request.POST.get('location')
        country = request.POST.get('country')
        activites_inc = request.POST.get('activites_included')
        activites_not = request.POST.get('activites_not_included')
        duration = request.POST.get('duration')
        price = request.POST.get('price')
        details = request.POST.get('details')

        package.title = title
        package.location = location
        package.country = country
        package.activites_inc = activites_inc
        package.activites_not = activites_not
        package.duration = duration
        package.price = price
        package.details = details
        package.updated_at = datetime.now()
        package.save()

        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            images = request.FILES.getlist('images')
            
            for image in images:
                handle_uploaded_file(image,"package")
                PackagesImage.objects.create(package = package,image =  "package/"+image.name,created_at = datetime.now(),
            updated_at = datetime.now(),)
        else:
            form = ImageForm()
            
            
        return redirect('/accounts/tour_management/')
    else:
        field_list =[
            Field("title",value=package.title),
            Field("location",value=package.location),
            Field("country",value=package.country),
            Field("activites_included",value=package.activites_inc),
            Field("activites_not_included",value=package.activites_not),
            Field("duration",value=package.duration),
            Field("price",value=package.price,type="number"),
            Field("details",value=package.details),
        ]
        item = "package"
        all_items = ["package","hotel","transport"]
        context = {"form":form,"item":item,"package":package,"item_images":package_images,"all_items":all_items,"fields":field_list}
        return render(request, 'accounts/edit_item.html', context)

def delete_image(request, item, item_id, image_id):
    if item == "package":
        obj = PackagesImage.objects.get(uid = image_id)
        obj.delete()
        return redirect("/accounts/edit_package/"+item_id)
    elif item == "hotel":
        obj = HotelImage.objects.get(uid = image_id)
        obj.delete()
        return redirect("/accounts/edit_hotel/"+item_id)
    elif item == "transport":
        obj = TransportImage.objects.get(uid = image_id)
        obj.delete()
        return redirect("/accounts/edit_hotel/"+item_id)
    
def delete_package(request, id):
    package = Packages.objects.get(uid = id)
    package.delete()
    return redirect("/accounts/tour_management")

def edit_hotel(request, id):

    form = ImageForm()
    hotel = Hotel.objects.get(uid = id)
    all_images = HotelImage.objects.all()
    hotel_images = []
    for image in all_images:
        if image.hotel == hotel:
            hotel_images.append(image)
        

    if request.method == "POST":
        name = request.POST.get('name')
        facilities = request.POST.get('facilities')
        location = request.POST.get('location')
        rooms = request.POST.get('rooms')
        country = request.POST.get('country')
        details = request.POST.get('details')
        price = request.POST.get('price')

        hotel.name = name
        hotel.location = location
        hotel.facilities = facilities
        hotel.rooms = rooms
        hotel.country = country
        hotel.price = price
        hotel.details = details
        hotel.updated_at = datetime.now()
        hotel.save()

        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            images = request.FILES.getlist('images')
            
            for image in images:
                handle_uploaded_file(image,"hotel")
                HotelImage.objects.create(hotel=hotel,image = "hotel/"+image.name,created_at = datetime.now(),
            updated_at = datetime.now(),)
        else:
            form = ImageForm()
            
            
        return redirect('/accounts/hotel_management/')
    else:
        field_list =[
            Field("name",hotel.name),
            Field("facilities", hotel.facilities),
            Field("location", hotel.location),
            Field("rooms", hotel.rooms),
            Field("country",hotel.country),
            Field("details", hotel.details),
            Field("price",hotel.price),
        ]
        item = "hotel"
        all_items = ["package","hotel","transport"]
        context = {"form":form,"item":item,"hotel":hotel,"item_images":hotel_images,"all_items":all_items,"fields":field_list}
        return render(request, 'accounts/edit_item.html', context)

def delete_hotel(request, id):
    hotel = Hotel.objects.get(uid = id)
    hotel.delete()
    return redirect("/accounts/hotel_management")

def edit_transport(request, id):

    form = ImageForm()
    transport = Transport.objects.get(uid = id)
    all_images = TransportImage.objects.all()
    transport_images = []
    for image in all_images:
        if image.transport == transport:
            transport_images.append(image)
        

    if request.method == "POST":
        make = request.POST.get('make')
        model = request.POST.get('model')
        varient = request.POST.get('varient')
        color = request.POST.get('color')
        year = request.POST.get('year')
        country = request.POST.get('country')
        seating_capacity = request.POST.get('seating_capacity')
        price = request.POST.get('price')

        transport.make = make
        transport.model = model
        transport.varient = varient
        transport.color = color
        transport.year = year
        transport.country = country
        transport.seating_capacity = seating_capacity
        transport.price = price
        
        transport.updated_at = datetime.now()
        transport.save()

        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            images = request.FILES.getlist('images')
            
            for image in images:
                handle_uploaded_file(image,"transport")
                TransportImage.objects.create(transport=transport,image = "transport/"+image.name,created_at = datetime.now(),
            updated_at = datetime.now(),)
        else:
            form = ImageForm()
            
            
        return redirect('/accounts/transport_management/')
    else:
        field_list =[
            Field("make", transport.make),
            Field("model",transport.model),
            Field("varient",transport.varient),
            Field("color",transport.color),
            Field("year",transport.year),
            Field("country",transport.country),
            Field("seating_capacity",transport.seating_capacity),
            Field("price",transport.price),
        ]
        item = "transport"
        all_items = ["package","hotel","transport"]
        context = {"form":form,"item":item,"transport":transport, "item_images":transport_images,"all_items":all_items,"fields":field_list}
        return render(request, 'accounts/edit_item.html', context)

def delete_transport(request, id):
    transport = Transport.objects.get(uid = id)
    transport.delete()
    return redirect("/accounts/transport_management")



def login_page(request):

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username=email)
        if not user_obj.exists():
            messages.warning(request, 'No account exist with this email')
            return HttpResponseRedirect(request.path_info)

        # if not user_obj[0].profile.is_email_verified:
        #      messages.warning(request, 'Your account is not verified')
        #      return HttpResponseRedirect(request.path_info)
            
        user_obj = authenticate(username = email, password=password)
        if user_obj:
            login(request, user_obj)
            return redirect('/')
        
        messages.warning(request, 'Invalid credentials')
        return HttpResponseRedirect(request.path_info)


    return render(request, 'accounts/login.html')


def register_page(request):
    
    if request.method == "POST":
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        country = request.POST.get('country')
        state = request.POST.get('state')
        city = request.POST.get('city')

        user_obj = User.objects.filter(username=email)
        if user_obj.exists():
            
            messages.warning(request, 'Email is already taken.')
            return HttpResponseRedirect(request.path_info)

        user_obj = User.objects.create(first_name=first_name,last_name=last_name,email=email,username=email)
        user_obj.set_password(password)
        user_obj.save()

        messages.success(request, 'You have successfully registered')
        return redirect('/accounts/login')

    return render(request, 'accounts/register.html')


def login_signup_page(request):

    if request.method == "POST":
        if request.POST.get('type') == "register":
            first_name = request.POST.get('firstname')
            last_name = request.POST.get('lastname')
            email = request.POST.get('email')
            password = request.POST.get('password')
            address = request.POST.get('address')
            country = request.POST.get('country')
            state = request.POST.get('state')
            city = request.POST.get('city')

            user_obj = User.objects.filter(username=email)
            if user_obj.exists():
                
                messages.warning(request, 'Email is already taken.')
                return HttpResponseRedirect(request.path_info)

            user_obj = User.objects.create(first_name=first_name,last_name=last_name,email=email,username=email)
            user_obj.set_password(password)
            user_obj.save()
            profile = Profile(
                user = user_obj,
                address = address,
                city = city,
                state = state,
                country = country,
                created_at = datetime.now(),
                updated_at = datetime.now(),
                )
            profile.save()

            messages.success(request, 'You have successfully registered')
            return redirect('/accounts/login_signup')

        elif request.POST.get('type') == "login":
            email = request.POST.get('email')
            password = request.POST.get('password')
            if email == "admin@gmail.com" and password == "admin":
                return redirect('/accounts/dashboard')

            user_obj = User.objects.filter(username=email)
            if not user_obj.exists():
                messages.warning(request, 'No account exist with this email')
                return HttpResponseRedirect(request.path_info)

            # if not user_obj[0].profile.is_email_verified:
            #      messages.warning(request, 'Your account is not verified')
            #      return HttpResponseRedirect(request.path_info)
                
            user_obj = authenticate(username = email, password=password)
            if user_obj:
                login(request, user_obj)
                
                return redirect('/')
            
            messages.warning(request, 'Invalid credentials')
            return HttpResponseRedirect(request.path_info)
        


    return render(request, 'accounts/login_signup.html')