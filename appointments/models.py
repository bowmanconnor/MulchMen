from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Appointment(models.Model):
    STATUS_CHOICES = [('P', 'Pending'), ('S', 'Scheduled'), ('C', 'Completed')]
    DELIVERY_CHOICES = [('P', 'I will set up the mulch delivery'), ('M', 'I would like MulchMen to set up the mulch delivery')]
    name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=254, blank=True, default="example@example.com")
    phone = PhoneNumberField(region='US', blank=True, help_text="Not required")
    address = models.CharField(help_text="Not required until appointment is confirmed", max_length=50,  blank=True)
    cubic_yards = models.PositiveIntegerField(blank=False, help_text="$25-35/cu. yard")
    weeding = models.BooleanField(blank=False, help_text="$5/cu. yard")
    bed_cleaning = models.BooleanField(blank=False, help_text="$5/cu. yard", default=False)
    edging = models.BooleanField(blank=False, help_text="$0.60/foot")
    delivery = models.CharField(max_length=1, choices=DELIVERY_CHOICES, default='P')
    date = models.DateField(auto_now=False, auto_now_add=False)
    status = models.CharField(default='P', max_length=1, choices=STATUS_CHOICES)
    cost = models.DecimalField(default=0, max_digits=16, decimal_places=2)
    sumbitted_at = models.DateTimeField(auto_now_add=True)
    hear_about_us = models.CharField(max_length=100, help_text="Facebook, reference, etc")
    additional_comments = models.CharField(max_length=2000, blank=True, help_text="Type of mulch, delivery instructions, quantity of mulch confusion, special requests, etc")

    user = models.ForeignKey(User, related_name='appointments', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name



class Expense(models.Model):
    expense = models.CharField(max_length=50, blank=False)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    purchaser = models.CharField(max_length=50, blank=False)
    paid = models.BooleanField(blank=False, default=False)

    def __str__(self):
        return self.expense
