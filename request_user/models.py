from django.db import models
from django.urls import reverse
import os
from datetime import datetime

# Create your models here.

STATUS = (
    (0, 'Inactive'),
    (1, 'Active'),
)

DISPLAY = (
    (0, 'No'),
    (1, 'Yes'),
)

class RequestUser(models.Model):
    class Meta:
        db_table = "wp_request_user"
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    mobile_no = models.CharField(max_length=50, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    pin_code = models.CharField(max_length=10, null=True, blank=True)
    services_need=models.CharField(max_length=200, null=True, blank=True)
    booking_date = models.DateTimeField(null=True, blank=True)
    budget = models.CharField(max_length=100, null=True, blank=True)
    total_person = models.CharField(max_length=100, null=True, blank=True)
    veg_non_veg = models.IntegerField(choices=DISPLAY, default=0)
    services_id = models.IntegerField(null=True, blank=True)
    services_cat_id = models.IntegerField(null=True, blank=True)
    country_id = models.IntegerField(null=True, blank=True)
    city_id = models.IntegerField(null=True, blank=True)
    location_id = models.IntegerField(null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    created_at = models.DateTimeField(null=True, blank=True)

    def summary(self):
        return self.description[:100]

    def pretty_created_date(self):
        return self.created_at.strftime('%b %e %Y')

    def pretty_updated_date(self):
        return self.updated_at.strftime('%b %e %Y')

    def __str__(self):
        return self.name

    def get_absolute_url(self):  # new
        return reverse('request_user:details', args=[str(self.id)])
