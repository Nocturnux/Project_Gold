# Generated by Django 5.0.1 on 2024-01-29 12:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cabin_type', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cabin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=255)),
                ('publication_date', models.DateField()),
                ('price', models.IntegerField()),
                ('image', models.ImageField(null=True, upload_to='cabin_images')),
                ('name', models.TextField(max_length=100)),
                ('status', models.BooleanField(default=True)),
                ('id_cabinType', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cabin_type.cabin_type')),
            ],
        ),
    ]
