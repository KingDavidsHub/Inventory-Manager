# Generated by Django 4.2.3 on 2023-07-10 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IT', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ititem',
            old_name='serial_number',
            new_name='location',
        ),
    ]
