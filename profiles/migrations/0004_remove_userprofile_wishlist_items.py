# Generated by Django 3.2 on 2022-02-18 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_userprofile_wishlist_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='wishlist_items',
        ),
    ]
