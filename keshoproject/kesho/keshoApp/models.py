from django.db import models
from django.utils import timezone

# Create your models here.


class Category_stay(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self) -> str:
        return self.name





class Babe(models.Model):
    c_stay = models.ForeignKey(
        Category_stay, on_delete=models.CASCADE, null=True, blank=True
    )
    # c_fee = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True)
    b_name = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True, default=1)
    gender = models.CharField(max_length=2, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    sponser = models.CharField(max_length=100, null=True, blank=True)
    time_in = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    time_out = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self) -> str:
        return self.b_name
    
class Payment(models.Model):
    payee = models.ForeignKey(Babe, on_delete=models.CASCADE, null=True, blank=True)
    c_payment = models.ForeignKey(
        Category_stay, on_delete=models.CASCADE, null=True, blank=True
    )
    amount = models.IntegerField(null=True, blank=True)
    payno = models.IntegerField(null=True, blank=True)
    currency = models.CharField(max_length=10, default="Ugx", null=True, blank=True)

    def __int__(self):
        return self.payee
