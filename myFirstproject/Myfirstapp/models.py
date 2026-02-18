from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    balance=models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.save()
            return True
        return False
    def deposit(self, amount):
        self.balance += amount
        self.save()