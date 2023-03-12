from django.db import models
from base.models import BaseModel
from django.utils.text import slugify
# Create your models here.

# Transport ------------------------------------------------------------------

class TransportCategory(BaseModel):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category_image = models.ImageField(upload_to="transport_categories")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(TransportCategory, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.category_name

class Transport(BaseModel):
    slug = models.SlugField(unique=True, null=True, blank=True)
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    varient = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    seating_capacity = models.CharField(max_length=200)
    price = models.IntegerField()
    ratings = models.CharField(max_length=200,null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.model)
        super(Transport, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.model

class TransportImage(BaseModel):
    transport = models.ForeignKey(Transport, on_delete=models.CASCADE, related_name="transport_image")
    image = models.ImageField(upload_to="transport")


# Hotels--------------------------------------------------------------------------------------------

class Hotel(BaseModel):
    slug = models.SlugField(unique=True, null=True, blank=True)
    name = models.CharField(max_length=200)
    facilities = models.CharField(max_length=500)
    location = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    rooms = models.CharField(max_length=200)
    details = models.CharField(max_length=1000)
    price = models.IntegerField()
    ratings = models.CharField(max_length=1000,null=True,blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Hotel, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


class HotelImage(BaseModel):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="hotel_image")
    image = models.ImageField(upload_to="hotel")





# package ------------------------------------------------------------------------------------------

class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category_image = models.ImageField(upload_to="categories")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.category_name


class Packages(BaseModel):
    title = models.CharField(max_length=500)
    slug = models.SlugField(unique=True, null=True, blank=True)
    activites_inc = models.CharField(max_length=500)
    activites_not = models.CharField(max_length=500)
    duration = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    details = models.TextField(max_length=1000)
    price = models.IntegerField()
    ratings = models.CharField(max_length=100,null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Packages, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title

class PackagesImage(BaseModel):
    package = models.ForeignKey(Packages, on_delete=models.CASCADE, related_name="package_image")
    image = models.ImageField()

    def __str__(self) -> str:
        return self.package.title
