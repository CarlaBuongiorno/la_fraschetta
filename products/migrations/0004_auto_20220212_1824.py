# Generated by Django 3.2 on 2022-02-12 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_rating_product_reviews'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='reviews',
            new_name='rating',
        ),
        migrations.AlterField(
            model_name='category',
            name='friendly_name',
            field=models.CharField(max_length=254, null=True),
        ),
    ]