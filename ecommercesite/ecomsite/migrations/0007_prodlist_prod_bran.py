# Generated by Django 4.0.4 on 2022-06-22 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecomsite', '0006_list_of_brands'),
    ]

    operations = [
        migrations.AddField(
            model_name='prodlist',
            name='prod_Bran',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='ecomsite.list_of_brands'),
        ),
    ]