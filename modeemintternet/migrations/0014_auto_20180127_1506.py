# Generated by Django 2.0.1 on 2018-01-27 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("modeemintternet", "0013_auto_20180127_1503")]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="ends",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="event",
            name="starts",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
