# Generated by Django 2.0.7 on 2019-11-11 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authe', '0004_auto_20191111_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profesion',
            field=models.CharField(default='NONE', max_length=50, verbose_name='Profession'),
        ),
    ]