from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#...Class DRIVER added here...
STATE_CHOICES = (
     ("Andhra Pradesh","Andhra Pradesh"),
     ("Arunachal Pradesh ","Arunachal Pradesh "),
     ("Assam","Assam"),
     ("Bihar","Bihar"),
     ("Chhattisgarh","Chhattisgarh"),
     ("Goa","Goa"),
     ("Gujarat","Gujarat"),
     ("Haryana","Haryana"),
     ("Himachal Pradesh","Himachal Pradesh"),
     ("Jammu and Kashmir ","Jammu and Kashmir "),
     ("Jharkhand","Jharkhand"),
     ("Karnataka","Karnataka"),
     ("Kerala","Kerala"),
     ("Madhya Pradesh","Madhya Pradesh"),
     ("Maharashtra","Maharashtra"),
     ("Manipur","Manipur"),
     ("Meghalaya","Meghalaya"),
     ("Mizoram","Mizoram"),
     ("Nagaland","Nagaland"),
     ("Odisha","Odisha"),
     ("Punjab","Punjab"),
     ("Rajasthan","Rajasthan"),
     ("Sikkim","Sikkim"),
     ("Tamil Nadu","Tamil Nadu"),
     ("Telangana","Telangana"),
     ("Tripura","Tripura"),
     ("Uttar Pradesh","Uttar Pradesh"),
     ("Uttarakhand","Uttarakhand"),
     ("West Bengal","West Bengal"),
     ("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),
     ("Chandigarh","Chandigarh"),
     ("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),
     ("Daman and Diu","Daman and Diu"),
     ("Lakshadweep","Lakshadweep"),
     ("National Capital Territory of Delhi","National Capital Territory of Delhi"),
     ("Puducherry","Puducherry")
)

CAR_CHOICES = (
    ("Micro","Micro"),
    ("Mini","Mini"),
    ("Prime Sedan","Prime Sedan"),
    ("Prime SUV","Prime SUV"),
)
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    locality = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=50, null=True)
    zipcode = models.IntegerField(null=True)
    state = models.CharField(choices=STATE_CHOICES, max_length=50, null=True)

    def __str__(self):
        return str(self.id)

class Driver(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    locality = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=50, null=True)
    zipcode = models.IntegerField(null=True)
    state = models.CharField(choices=STATE_CHOICES, max_length=50, null=True)
    car = models.CharField(choices=CAR_CHOICES, max_length=50, null=True)
    number = models.IntegerField(null=True)

    def __str__(self):
        return str(self.id)


class Car(models.Model):
    car_brand = models.CharField(max_length=50)
    number_plate = models.CharField(max_length=20)
    seat_number = models.CharField(max_length=20)

    def __str__(self):
        return self.car_brand

class Location(models.Model):
    longitude = models.CharField(max_length=10)
    latitude = models.CharField(max_length=10)
    location_name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.location_name

class Category(models.Model):
    pickup_location = models.CharField(max_length=20)
    arrival_destination = models.CharField(max_length=20)

    def __str__(self):
        return self.pickup_location

class Search(models.Model):
    address = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address