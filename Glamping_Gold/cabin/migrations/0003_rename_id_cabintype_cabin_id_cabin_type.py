# Generated by Django 5.0.1 on 2024-01-30 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cabin', '0002_rename_price_cabin_value_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cabin',
            old_name='id_cabinType',
            new_name='id_cabin_type',
        ),
    ]
