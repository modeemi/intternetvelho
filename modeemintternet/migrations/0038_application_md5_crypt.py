# Generated by Django 3.1.7 on 2021-02-23 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("modeemintternet", "0037_auto_20210222_2113"),
    ]

    operations = [
        migrations.AddField(
            model_name="application",
            name="md5_crypt",
            field=models.CharField(default="", max_length=128),
            preserve_default=False,
        ),
    ]
