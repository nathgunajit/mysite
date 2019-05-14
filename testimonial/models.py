from django.db import models

# Create your models here.


class Testimonial(models.Model):
    class Meta:
        db_table = "wp_testimonial"
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='testimonial/images/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    display_home = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
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