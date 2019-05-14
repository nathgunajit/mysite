from django.db import models


class Payment(models.Model):
    class Meta:
        db_table = "wp_payment"
    user_id = models.IntegerField()
    user_type = models.IntegerField()
    package_id = models.IntegerField()
    country_id = models.IntegerField()
    payment_gateway = models.IntegerField(null=True, blank=True)
    transaction_id = models.CharField(max_length=100,null=True, blank=True)
    payment_status = models.IntegerField(null=True, blank=True)
    transaction_time = models.DateTimeField()
