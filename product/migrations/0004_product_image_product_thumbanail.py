# Generated by Django 4.1.2 on 2022-10-25 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='product',
            name='thumbanail',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]