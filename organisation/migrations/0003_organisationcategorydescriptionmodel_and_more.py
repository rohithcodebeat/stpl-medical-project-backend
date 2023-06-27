# Generated by Django 4.2.2 on 2023-06-27 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "organisation",
            "0002_organisationcategorymodel_organisationmodel_address_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="OrganisationCategoryDescriptionModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.TextField(blank=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name="organisationcategorymodel",
            name="description",
        ),
        migrations.AddField(
            model_name="organisationcategorymodel",
            name="description",
            field=models.ManyToManyField(
                blank=True,
                related_name="OrganisationCategoryModel_description",
                to="organisation.organisationcategorydescriptionmodel",
            ),
        ),
    ]