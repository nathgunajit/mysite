from django.db import models
from category.models import Category
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):

    STATUS = (
        (0, 'Inactive'),
        (1, 'Active'),
    )

    DISPLAY = (
        (0, 'No'),
        (1, 'Yes'),
    )

    class Meta:
        db_table = "wp_blog"
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog/images/', null=True, blank=True)
    small_description = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    author = models.CharField(max_length=100)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    meta_title = models.CharField(max_length=250, null=True, blank=True)
    meta_keyword = models.CharField(max_length=250, null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)
    display_home = models.IntegerField(choices=DISPLAY, default=0)
    display_menu = models.IntegerField(choices=DISPLAY, default=0)
    status = models.IntegerField(choices=STATUS, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    created_user=models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)

    def summary(self):
        return self.description[:100]

    def pretty_created_date(self):
        return self.created_at.strftime('%b %e %Y')

    def pretty_updated_date(self):
        return self.updated_at.strftime('%b %e %Y')

    def __str__(self):
        return self.name