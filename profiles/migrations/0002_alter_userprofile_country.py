# Generated by Django 3.2 on 2022-02-10 22:05

from django.db import migrations
import django_countries.fields
import profiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='country',
            field=django_countries.fields.CountryField(blank=True, countries=profiles.models.UserProfile.G8Countries, max_length=80, null=True),
        ),
    ]