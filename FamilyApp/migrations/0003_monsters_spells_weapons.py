# Generated by Django 4.1.5 on 2023-02-06 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("FamilyApp", "0002_alter_familiar_edad"),
    ]

    operations = [
        migrations.CreateModel(
            name="Monsters",
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
                ("nombre", models.CharField(max_length=30)),
                ("nivel_desafio", models.IntegerField()),
                ("terreno", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="Spells",
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
                ("nombre", models.CharField(max_length=30)),
                ("nivel", models.IntegerField()),
                ("escuela", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="Weapons",
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
                ("nombre", models.CharField(max_length=30)),
                ("tipo", models.CharField(max_length=30)),
                ("versatil", models.BooleanField()),
            ],
        ),
    ]
