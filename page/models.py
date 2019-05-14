from django.db import models

# Create your models here.

class Page(models.Model):
    class Meta:
        db_table = "wp_page"
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pages/images/', null=True, blank=True)
    icon = models.ImageField(upload_to='pages/images/icon/', null=True, blank=True)
    font_icon = models.CharField(max_length=200, null=True, blank=True)
    small_description = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    meta_title = models.CharField(max_length=250, null=True, blank=True)
    meta_keyword = models.CharField(max_length=250, null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)
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