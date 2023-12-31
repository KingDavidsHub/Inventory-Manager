# Generated by Django 4.2.3 on 2023-07-11 17:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('IT', '0006_rename_service_tag_ititem_ser_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='ITStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('total', models.CharField(default='', max_length=200)),
                ('amount_assigned', models.CharField(default='', max_length=200)),
                ('amount_left', models.TextField(default='', max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='it_store', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
