# Generated by Django 2.2.4 on 2019-08-27 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("modeemintternet", "0029_auto_20190827_2052")]

    operations = [
        migrations.RenameField(
            model_name="membership", old_name="city", new_name="municipality"
        )
    ]
