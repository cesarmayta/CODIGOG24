# Generated by Django 4.2 on 2024-02-28 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_alter_productoimagen_options_producto_sku_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='sku',
            field=models.CharField(max_length=10, null=True, unique=True),
        ),
    ]
