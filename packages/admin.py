from django.contrib import admin
from .models import *

# Register your models here.
# packages------------------------------------
admin.site.register(Category)

class PackageImageAdmin(admin.StackedInline):
    model = PackagesImage

class PackageAdmin(admin.ModelAdmin):
    inlines = [PackageImageAdmin]

admin.site.register(Packages, PackageAdmin)
admin.site.register(PackagesImage)

# transport --------------------------------
admin.site.register(TransportCategory)

class TransportImageAdmin(admin.StackedInline):
    model = TransportImage

class TransportAdmin(admin.ModelAdmin):
    inlines = [TransportImageAdmin]

admin.site.register(Transport, TransportAdmin)
admin.site.register(TransportImage)

# Hotel--------------------------------
class HotelImageAdmin(admin.StackedInline):
    model = HotelImage

class HotelAdmin(admin.ModelAdmin):
    inlines = [HotelImageAdmin]

admin.site.register(Hotel, HotelAdmin)
admin.site.register(HotelImage)
