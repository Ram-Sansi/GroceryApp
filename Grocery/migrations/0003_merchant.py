# Generated by Django 4.2 on 2023-04-11 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Grocery', '0002_alter_grocery_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=255)),
                ('shop_name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=255)),
            ],
        ),
    ]
