# Generated by Django 2.2.4 on 2019-08-07 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("modeemintternet", "0026_auto_20190807_1654")]

    operations = [
        migrations.AlterField(
            model_name="membership",
            name="fee",
            field=models.ManyToManyField(
                blank=True,
                to="modeemintternet.MembershipFee",
                verbose_name="Jäsenmaksut",
            ),
        )
    ]
