# Generated by Django 2.2.4 on 2019-08-27 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("modeemintternet", "0028_auto_20190826_1825")]

    operations = [
        migrations.AlterField(
            model_name="membership",
            name="city",
            field=models.CharField(
                blank=True, default="", max_length=128, verbose_name="Kotipaikka"
            ),
        )
    ]
