from django.db import models

# Create your models here.


class Package(models.Model):
    class Meta:
        db_table = "wp_package"
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, null=True, blank=True)
    price = models.CharField(max_length=20, null=True, blank=True)
    duration = models.CharField(max_length=50, null=True, blank=True)
    user_type = models.IntegerField(null=True, blank=True)
    country = models.IntegerField(null=True, blank=True)
    currency = models.CharField(max_length=20, null=True, blank=True)
    image = models.ImageField(upload_to='package/images/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    display_home = models.IntegerField(default=0)
    display_menu = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
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