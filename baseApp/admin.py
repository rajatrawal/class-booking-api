from django.contrib import admin

# Register your models here.


from .models import ClassBooking,FitnessClass

admin.site.register((FitnessClass,ClassBooking))
