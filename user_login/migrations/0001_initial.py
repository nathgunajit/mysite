# Generated by Django 2.1.4 on 2019-05-13 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserLogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('user_type', models.IntegerField()),
                ('user_name', models.CharField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(blank=True, max_length=255, null=True)),
                ('token', models.CharField(blank=True, max_length=255, null=True)),
                ('is_active', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('subscribe', models.IntegerField(default=0)),
                ('package_id', models.IntegerField(default=0)),
                ('duration', models.IntegerField(blank=True, null=True)),
                ('subscribe_date', models.DateTimeField()),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('device_id', models.CharField(blank=True, max_length=200, null=True)),
                ('ip_address', models.IntegerField(blank=True, null=True)),
                ('is_login', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'wp_user_login',
            },
        ),
    ]