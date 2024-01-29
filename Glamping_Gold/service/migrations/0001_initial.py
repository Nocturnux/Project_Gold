# Generated by Django 5.0.1 on 2024-01-29 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(null=True, upload_to='service_images')),
                ('description', models.TextField(max_length=255)),
                ('value', models.IntegerField()),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]
