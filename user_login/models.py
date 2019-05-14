from django.db import models


class UserLogin(models.Model):
    class Meta:
        db_table = "wp_user_login"
    user_id = models.IntegerField()
    user_type = models.IntegerField()
    user_name = models.CharField(max_length=100,null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    token = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.IntegerField(default=0)
    created_at = models.DateTimeField(null=True, blank=True)
    subscribe = models.IntegerField(default=0)
    package_id = models.IntegerField(default=0)
    duration = models.IntegerField(null=True, blank=True)
    subscribe_date = models.DateTimeField()
    last_login = models.DateTimeField(null=True, blank=True)
    device_id = models.CharField(max_length=200,null=True, blank=True)
    ip_address = models.IntegerField(null=True, blank=True)
    is_login = models.DateTimeField(null=True, blank=True)
