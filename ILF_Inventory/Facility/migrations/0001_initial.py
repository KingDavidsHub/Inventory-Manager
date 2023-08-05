# Generated by Django 4.2.3 on 2023-07-15 22:28

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FacilityItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('location', models.CharField(default='', max_length=200)),
                ('tag', models.CharField(default='', max_length=200)),
                ('owner', models.CharField(default='', max_length=200)),
                ('date_purchased', models.DateField(default=datetime.date.today)),
                ('warranty_period', models.IntegerField(default=10)),
                ('warranty_expired', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='facility_items', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]