# Generated by Django 4.2.2 on 2023-06-15 12:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organisation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganisationCategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('sub_title', models.CharField(blank=True, max_length=500, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='OrganisationCategoryModel_category', to='organisation.categorymodel')),
                ('icon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='OrganisationCategoryModel_icon', to='organisation.organisationmediagallerymodel')),
                ('media', models.ManyToManyField(blank=True, related_name='OrganisationCategoryModel_media', to='organisation.organisationmediagallerymodel')),
            ],
        ),
        migrations.AddField(
            model_name='organisationmodel',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='OrganisationModel_address', to='address.addressmodel'),
        ),
        migrations.AddField(
            model_name='organisationmodel',
            name='org_type',
            field=models.CharField(blank=True, choices=[('DIAGNOSIS', 'DIAGNOSIS'), ('HOSPITAL', 'HOSPITAL'), ('OTHER', 'OTHER')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='organisationmodel',
            name='x_coordinate',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='organisationmodel',
            name='y_coordinate',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='OrganisationDoctorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='OrganisationDoctorModel_category', to='organisation.organisationcategorymodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='OrganisationDoctorModel_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='organisationcategorymodel',
            name='organisation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='OrganisationCategoryModel_organisation', to='organisation.organisationmodel'),
        ),
    ]
