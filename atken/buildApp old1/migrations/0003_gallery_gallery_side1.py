# Generated by Django 3.2 on 2021-10-02 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buildApp', '0002_auto_20211002_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='gallery_side1',
            field=models.ImageField(blank=True, null=True, upload_to='gallery'),
        ),
    ]
