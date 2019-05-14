from django.db import models
from category.models import Category
from countries.models import Countries, Cities, Location
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class WeddingImages(models.Model):

    STATUS = (
        (0, 'Inactive'),
        (1, 'Active'),
    )

    DISPLAY = (
        (0, 'No'),
        (1, 'Yes'),
    )

    class Meta:
        db_table = "wp_wedding_images"
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    wedding_date = models.DateField(null=True, blank=True)
    country = models.ForeignKey(Countries, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(Cities, on_delete=models.SET_NULL, null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='wedding/images/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    meta_title = models.CharField(max_length=250, null=True, blank=True)
    meta_keyword = models.CharField(max_length=250, null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)
    display_home = models.IntegerField(choices=DISPLAY, default=0)
    display_menu = models.IntegerField(choices=DISPLAY, default=0)
    status = models.IntegerField(choices=STATUS, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    created_user=models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)

    def summary(self):
        return self.description[:100]

    def pretty_created_date(self):
        return self.created_at.strftime('%b %e %Y')

    def pretty_wedding_date(self):
        return self.wedding_date.strftime('%b %e %Y')

    def __str__(self):
        return self.name