# Generated by Django 4.1.7 on 2023-02-23 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FamilyApp', '0010_alter_weapons_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weapons',
            name='descripcion',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='weapons',
            name='opinion',
            field=models.TextField(default='nadie opinó aún', max_length=1000),
        ),
    ]
