# Generated by Django 4.2.2 on 2023-07-03 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slot_booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisationslotbookingmodel',
            name='status',
            field=models.CharField(choices=[('PENDING', 'PENDING'), ('UPCOMING', 'UPCOMING'), ('COMPLETED', 'COMPLETE'), ('FAILED', 'FAILED'), ('CANCELLED', 'CANCELLED')], default='PENDING', max_length=100),
        ),
    ]
