# Generated by Django 4.0.4 on 2022-06-22 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomsite', '0008_remove_prodlist_prod_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='list_of_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='list_of_Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=50)),
            ],
        ),
    ]