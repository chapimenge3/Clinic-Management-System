# Generated by Django 2.0.7 on 2019-11-10 11:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0005_auto_20191110_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='token_num',
            field=models.PositiveIntegerField(default=1, unique=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='id'),
        ),
    ]
