# Generated by Django 2.1.10 on 2019-08-18 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20190818_0212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='assign_days',
            field=models.PositiveSmallIntegerField(blank=True, default='', null=True),
        ),
    ]
