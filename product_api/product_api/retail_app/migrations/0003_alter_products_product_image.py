# Generated by Django 4.1.3 on 2023-02-10 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retail_app', '0002_products_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_image',
            field=models.ImageField(default='None.jpg', upload_to='retail_app/media'),
        ),
    ]
