# Generated by Django 4.1.3 on 2023-02-10 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('retail_app', '0005_remove_cartitems_total_items_products_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitems',
            name='product',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='retail_app.products'),
        ),
    ]
