# Generated by Django 5.2 on 2025-05-23 13:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='product',
            field=models.ForeignKey(default='001', on_delete=django.db.models.deletion.CASCADE, to='products.products'),
        ),
    ]
