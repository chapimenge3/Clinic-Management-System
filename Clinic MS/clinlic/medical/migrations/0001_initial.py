# Generated by Django 2.0.7 on 2019-11-10 09:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token_num', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('toke', models.CharField(max_length=50)),
            ],
        ),
    ]
