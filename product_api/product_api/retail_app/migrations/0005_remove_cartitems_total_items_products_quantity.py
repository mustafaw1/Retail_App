# Generated by Django 4.1.3 on 2023-02-10 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retail_app', '0004_cart_cartitems'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitems',
            name='total_items',
        ),
        migrations.AddField(
            model_name='products',
            name='quantity',
            field=models.IntegerField(default=0, max_length=200),
        ),
    ]
