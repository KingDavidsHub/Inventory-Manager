# Generated by Django 4.2.3 on 2023-07-10 16:23

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
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'project',
            },
        ),
        migrations.CreateModel(
            name='ITItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_name', models.CharField(default='', max_length=200)),
                ('devices', models.CharField(default='', max_length=200)),
                ('model', models.CharField(default='', max_length=200)),
                ('serial_number', models.CharField(default='', max_length=200)),
                ('technical_description', models.TextField(default='', max_length=200)),
                ('computer_name', models.CharField(default='', max_length=200)),
                ('service_tag', models.CharField(default='', max_length=200)),
                ('win_version', models.IntegerField(default=10)),
                ('supplier', models.CharField(default='', max_length=200)),
                ('date_purchased', models.DateField(default=datetime.date.today)),
                ('warranty_period', models.DateField(default=datetime.date.today)),
                ('warranty_expired', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('comment', models.CharField(default='', max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='IT.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='it_items', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
