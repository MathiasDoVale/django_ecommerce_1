# Generated by Django 3.1.2 on 2020-11-08 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_media'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='can_backorder',
            field=models.BooleanField(default=False),
        ),
    ]