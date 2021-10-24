# Generated by Django 3.2.5 on 2021-10-24 19:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_auto_20211018_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(50), django.core.validators.MaxValueValidator(100000)], verbose_name='price'),
        ),
    ]
