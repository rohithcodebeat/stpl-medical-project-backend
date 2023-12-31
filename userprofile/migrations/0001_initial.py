# Generated by Django 4.2.2 on 2023-06-27 06:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('slot_booking', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileMediaGalleryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.URLField(blank=True, max_length=1000, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pics', models.URLField(blank=True, max_length=1000, null=True)),
                ('date_of_birth', models.DateTimeField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHER', 'OTHER')], max_length=25, null=True)),
                ('height', models.FloatField(blank=True, null=True)),
                ('weight', models.FloatField(blank=True, null=True)),
                ('blood_group', models.CharField(blank=True, choices=[('O_POSITIVE', 'O_POSITIVE'), ('O_NEGITIVE', 'O_NEGITIVE'), ('A_POSITIVE', 'A_POSITIVE'), ('A_NEGITIVE', 'A_NEGITIVE'), ('B_POSITIVE', 'B_POSITIVE'), ('B_NEGITIVE', 'B_NEGITIVE'), ('AB_POSITIVE', 'AB_POSITIVE'), ('AB_NEGITIVE', 'AB_NEGITIVE'), ('OTHERS', 'OTHERS')], max_length=25, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='UserProfileModel_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserCartModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('slot', models.ManyToManyField(blank=True, related_name='UserCartModel_slot', to='slot_booking.organisationslotbookingmodel')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='UserCartModel_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
