from django.db import models
from django.utils import timezone
# Create your models here.



# Fitness class model 
class FitnessClass(models.Model):
    name = models.CharField(max_length=256)
    datetime = models.DateTimeField()
    teacher = models.CharField(max_length=256)
    total_slots = models.PositiveIntegerField()
    available_slots = models.PositiveIntegerField(default=0,blank=True)
    fees = models.PositiveIntegerField(default=0)


    def __str__(self):
        return f"{self.name} on {self.datetime.strftime('%Y-%m-%d %H:%M')}"

    def save(self,*args, **kwargs):
        if not self.pk:
            self.available_slots = self.total_slots
        return super().save(*args, **kwargs)
    

#Booking model

class ClassBooking(models.Model):
    fitness_class = models.ForeignKey(FitnessClass,on_delete=models.CASCADE,related_name='bookings')
    client_name = models.CharField(max_length=256)
    client_email = models.EmailField()
    phone_number = models.CharField(max_length=12)
    booking_datetime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.client_name} - {self.fitness_class.name}"
