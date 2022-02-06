# Generated by Django 3.2 on 2022-02-06 13:40

import checkout.models
from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_country',
            field=django_countries.fields.CountryField(countries=checkout.models.Order.G8Countries, max_length=80),
        ),
    ]
