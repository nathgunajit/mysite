from django.db import models

# Create your models here.


class Banner(models.Model):
    class Meta:
        db_table = "wp_banner"
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    link_url = models.CharField(max_length=100,null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='banner/images/', null=True, blank=True)
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