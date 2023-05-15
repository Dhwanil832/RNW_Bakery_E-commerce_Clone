# Generated by Django 4.0.4 on 2022-06-22 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecomsite', '0009_list_of_category_list_of_supplier'),
    ]

    operations = [
        migrations.AddField(
            model_name='prodlist',
            name='prod_cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='ecomsite.list_of_category'),
        ),
        migrations.AddField(
            model_name='prodlist',
            name='prod_supp',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='ecomsite.list_of_supplier'),
        ),
    ]