# Generated by Django 4.1.2 on 2022-10-25 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_image_product_thumbanail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='thumbanail',
            new_name='thumbnail',
        ),
    ]
