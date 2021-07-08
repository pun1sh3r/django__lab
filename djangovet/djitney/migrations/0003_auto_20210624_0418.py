# Generated by Django 3.0.5 on 2021-06-24 04:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('djitney', '0002_auto_20210624_0305'),
    ]

    operations = [
        migrations.AddField(
            model_name='line',
            name='schedule',
            field=models.TimeField(default=datetime.datetime(2021, 6, 24, 4, 18, 42, 407893, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='station',
            name='last_cleaned_date',
            field=models.DateField(default=datetime.datetime(2021, 6, 24, 4, 18, 42, 408182, tzinfo=utc)),
        ),
    ]
