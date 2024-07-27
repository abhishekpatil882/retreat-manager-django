from django.db import models

class Retreat(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField()
    description = models.TextField()

class Booking(models.Model):
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=255)
    user_email = models.EmailField()
    user_phone = models.CharField(max_length=20)
    retreat = models.ForeignKey(Retreat, on_delete=models.CASCADE)
    payment_details = models.TextField()
    booking_date = models.DateField()