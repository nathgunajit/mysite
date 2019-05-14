from django.db import models
from django.contrib.auth.models import User
from countries.models import Countries, Cities, Location
from category.models import Category, SubCategory
from services_category.models import ServicesCategory,ServicesSubcategory
# Create your models here.

STATUS = (
    (0, 'Inactive'),
    (1, 'Active'),
)

DISPLAY = (
    (0, 'No'),
    (1, 'Yes'),
)


class Venue(models.Model):
    class Meta:
        db_table = "wp_venue"
    name=models.CharField(max_length=200)
    title = models.CharField(max_length=200, blank=True)
    vendor_id = models.IntegerField(null=True, blank=True)
    start_year =models.CharField(max_length=20,blank=True)
    email_id = models.EmailField(max_length=50, blank=True)
    phone_no = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=200, blank=True)
    pin_code = models.IntegerField(null=True, blank=True)
    loc_id = models.ForeignKey(Location, null=True, blank=True, on_delete=models.CASCADE)
    city_id = models.ForeignKey(Cities, null=True, blank=True, on_delete=models.CASCADE)
    country_id = models.ForeignKey(Countries, null=True, blank=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, null=True, blank=True, on_delete=models.CASCADE)
    service = models.ForeignKey(ServicesCategory, null=True, blank=True, on_delete=models.CASCADE)
    small_description = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    gurden_space = models.CharField(max_length=200, blank=True)
    total_capacity = models.CharField(max_length=200, blank=True)
    is_hall = models.IntegerField(choices=DISPLAY, default=0)
    hall_capacity = models.CharField(max_length=200, blank=True)
    setting_capacity = models.CharField(max_length=200, blank=True)
    is_parking_capacity = models.IntegerField(choices=DISPLAY, default=0)
    parking_capacity = models.CharField(max_length=200, blank=True)
    total_washroom = models.CharField(max_length=200, blank=True)
    area_space = models.CharField(max_length=200, blank=True)
    price_start= models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='vendor/images/', null=True, blank=True)
    front_image = models.ImageField(upload_to='vendor/front/images/', null=True, blank=True)
    gallery_image = models.ImageField(upload_to='vendor/gallery/images/', null=True, blank=True)
    is_latest = models.IntegerField(choices=DISPLAY, default=0)
    display_home = models.IntegerField(default=0)
    created_at = models.DateTimeField(null=True, blank=True)
    created_user = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_user = models.IntegerField(null=True, blank=True)
    website_url = models.CharField(max_length=100,blank=True)
    views = models.IntegerField(default=0)
    status = models.IntegerField(choices=STATUS, default=0)

    def summary(self):
        return self.description[:100]

    def pretty_created_date(self):
        return self.created_at.strftime('%b %e %Y')

    def pretty_updated_date(self):
        return self.updated_at.strftime('%b %e %Y')

    def __str__(self):
        return self.name