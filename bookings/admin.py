from django.contrib import admin
from .models import Booking, Trips

# Register your models here.


class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class TripAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Booking, BookingAdmin)
admin.site.register(Trips, TripAdmin)
