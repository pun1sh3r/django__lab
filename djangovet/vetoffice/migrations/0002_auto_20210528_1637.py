# Generated by Django 3.0.5 on 2021-05-28 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vetoffice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='breed',
            field=models.CharField(max_length=201),
        ),
        migrations.AlterField(
            model_name='patient',
            name='pet_name',
            field=models.CharField(max_length=201),
        ),
    ]
