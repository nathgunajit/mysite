from django.db import models

# Create your models here.


class Images(models.Model):
    class Meta:
        db_table = "wp_images"
    user_id = models.IntegerField()
    user_type = models.IntegerField()
    image_type = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='uploads/images/', null=True, blank=True)
    display_home = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(null=True, blank=True)
    created_user = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_user = models.IntegerField(null=True, blank=True)

    def pretty_created_date(self):
        return self.created_at.strftime('%b %e %Y')

    def pretty_updated_date(self):
        return self.updated_at.strftime('%b %e %Y')