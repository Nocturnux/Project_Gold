# Generated by Django 5.0.1 on 2024-01-29 14:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('booking', '0001_initial'),
        ('cabin', '0002_rename_price_cabin_value_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking_cabin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='booking.booking')),
                ('cabin', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cabin.cabin')),
            ],
        ),
    ]
