# Generated by Django 2.0.7 on 2019-11-09 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Last Name'),
        ),
    ]
