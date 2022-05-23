# Generated by Django 2.1.10 on 2019-08-14 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0010_auto_20190813_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='leave_type',
            field=models.CharField(choices=[('Sick leave', 'Sick'), ('Vacation leave', 'Vacation'), ('End of employee leave', 'End of Employee'), ('Maternity leave', 'Maternity Leave')], default='Sick leave', max_length=25, null=True),
        ),
    ]
