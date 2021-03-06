from django.db import models
from django.contrib.auth.models import User

class Supplier(models.Model):
    class Meta:
        db_table = "wp_supplier"
    name=models.CharField(max_length=200)
    title = models.CharField(max_length=200, blank=True)
    owner_name = models.CharField(max_length=200,blank=True)
    start_year =models.CharField(max_length=20,blank=True)
    email_id = models.CharField(max_length=50, blank=True)
    phone_no = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=200, blank=True)
    pin_code = models.IntegerField(null=True, blank=True)
    loc_id = models.IntegerField(null=True, blank=True)
    city_id = models.IntegerField(null=True, blank=True)
    country_id = models.IntegerField(null=True, blank=True)
    cat_id = models.IntegerField(null=True, blank=True)
    sub_cat_id = models.IntegerField(null=True, blank=True)
    services_id = models.IntegerField(null=True, blank=True)
    image=models.ImageField(upload_to='vendor/images/',null=True, blank=True)
    description=models.TextField(null=True, blank=True)
    display_home = models.IntegerField(default=0)
    subscription_type = models.IntegerField(default=0)
    package_id = models.IntegerField(default=0)
    created_at = models.DateTimeField(null=True, blank=True)
    #created_user = models.ForeignKey(User, on_delete=models.CASCADE)
    #updated_user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_user = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_user = models.IntegerField(null=True, blank=True)
    website_url =models.CharField(max_length=100,blank=True)
    views = models.IntegerField(default=0)
    status = models.IntegerField(default=0)

    def summary(self):
        return self.description[:100]

    def pretty_created_date(self):
        return self.created_at.strftime('%b %e %Y')

    def pretty_updated_date(self):
        return self.updated_at.strftime('%b %e %Y')

    def __str__(self):
        return self.name


class SupplierProduct(models.Model):
    class Meta:
        db_table = "wp_supplier_product"
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    product_type = models.IntegerField(null=True, blank=True)
    cat_id = models.DateTimeField(null=True, blank=True)
    subcat_id = models.CharField(max_length=200,null=True, blank=True)
    image = models.ImageField(upload_to='supplier_product/images/',null=True, blank=True)
    price = models.CharField(max_length=50, null=True, blank=True)
    quantity = models.CharField(max_length=50, null=True, blank=True)
    exp_date = models.DateTimeField(null=True, blank=True)
    stock = models.IntegerField(default=0)
    supplier_id = models.IntegerField(null=True, blank=True)
    status = models.IntegerField(default=0)
    display_home = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(null=True, blank=True)
    created_user = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_user = models.IntegerField(null=True, blank=True)

    def summary(self):
        return self.description[:100]

    def pretty_created_date(self):
        return self.created_at.strftime('%b %e %Y')

    def pretty_updated_date(self):
        return self.updated_at.strftime('%b %e %Y')

    def __str__(self):
        return self.name
