# Generated by Django 4.2 on 2023-04-15 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Grocery', '0008_alter_products_discount_alter_products_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='discount',
            field=models.IntegerField(),
        ),
    ]
