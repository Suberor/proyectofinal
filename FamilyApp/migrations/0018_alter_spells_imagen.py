# Generated by Django 4.1.7 on 2023-02-24 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FamilyApp', '0017_alter_spells_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spells',
            name='imagen',
            field=models.ImageField(default='FamilyApp/assets/img/blank.png', upload_to='FamilyApp/static/FamilyApp/assets/img/'),
        ),
    ]