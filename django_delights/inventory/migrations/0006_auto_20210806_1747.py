# Generated by Django 3.0.5 on 2021-08-06 17:47

from django.db import migrations
import inventory.models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_auto_20210806_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='title',
            field=inventory.models.NameField(max_length=30, unique=True),
        ),
    ]
