from django.db import models

class Countries(models.Model):
    class Meta:
        db_table = "wp_countries"
    name = models.CharField(max_length=50)
    country_code = models.CharField(max_length=20)
    display_home = models.IntegerField(default=0)
    display_menu = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(null=True, blank=True)
    created_user = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_user = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return '%s - %s ' % (self.name,self.country_code)


class Cities(models.Model):
    class Meta:
        db_table = "wp_cities"
    name = models.CharField(max_length=50)
    city_code = models.CharField(max_length=20)
    country = models.ForeignKey(Countries, on_delete=models.CASCADE)
    display_home = models.IntegerField(default=0)
    display_menu = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(null=True, blank=True)
    created_user = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_user = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    def city_name(self, city):
        return self.filter(id__icontains=city)

class Location(models.Model):
    class Meta:
        db_table = "wp_location"
    name = models.CharField(max_length=50)
    #loc_code = models.CharField(max_length=20)
    city = models.ForeignKey(Cities, on_delete=models.CASCADE)
    country = models.ForeignKey(Countries, on_delete=models.CASCADE)
    display_home = models.IntegerField(default=0)
    display_menu = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(null=True, blank=True)
    created_user = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_user = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

