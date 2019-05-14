from django.db import models
from django.urls import reverse,resolve
import os
from datetime import datetime
# Create your models here.
USER_TYPE = (
    (1, 'Vendor'),
    (2, 'Supplier'),
)
STATUS = (
    (0, 'Inactive'),
    (1, 'Active'),
)

DISPLAY = (
    (0, 'No'),
    (1, 'Yes'),
)


class Category(models.Model):

    def get_upload_path(instance, filename):
        return os.path.join('category/images/', datetime.now().date().strftime("%Y/%m/%d"), filename)

    class Meta:
        db_table = "wp_category"
        #get_latest_by = "created_at"
        ordering = ['-created_at']
        verbose_name = "category"
        verbose_name_plural = "categories"
        #unique_together = ['name', 'title']
        #indexes = [
        #    models.Index(fields=['name', 'title']),
        #    models.Index(fields=['name'], name='title_idx'),
        #]

    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True, upload_to=get_upload_path)
    description = models.TextField(null=True, blank=True)
    user_type = models.IntegerField(choices=USER_TYPE, default=1)
    display_home = models.IntegerField(choices=DISPLAY, default=0)
    display_menu = models.IntegerField(choices=DISPLAY, default=0)
    status = models.IntegerField(choices=STATUS, default=0)
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(null=True, blank=True)
    created_user = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_user = models.IntegerField(null=True, blank=True)
    #owner = models.ForeignKey(Owner, related_name='items')

    def summary(self):
        return self.description[:100]


    def pretty_created_date(self):
        return self.created_at.strftime('%b %e %Y')

    def pretty_updated_date(self):
        return self.updated_at.strftime('%b %e %Y')

    def __str__(self):
        return self.name

    def get_absolute_url(self): # new
        return reverse('category:details', args=[str(self.id)])

   #def url_custom(self):
    #    return 'category/%s' % (self.id)


class SubCategory(models.Model):
    class Meta:
        db_table = "wp_subcategory"
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='subcategory/images/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    user_type = models.IntegerField(choices=USER_TYPE, null=True, blank=True)
    cat_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    display_home = models.IntegerField(choices=DISPLAY, default=0)
    display_menu = models.IntegerField(choices=DISPLAY, default=0)
    status = models.IntegerField(choices=STATUS, default=0)
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