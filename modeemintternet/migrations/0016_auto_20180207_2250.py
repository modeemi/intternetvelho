# Generated by Django 2.0 on 2018-02-07 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modeemintternet', '0015_application_virtual_key_required'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passwd',
            fields=[
                ('username', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('uid', models.IntegerField()),
                ('gid', models.IntegerField()),
                ('gecos', models.CharField(max_length=255)),
                ('home', models.CharField(max_length=255)),
                ('shell', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'passwd',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Shadow',
            fields=[
                ('username', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('lastchanged', models.IntegerField()),
                ('min', models.IntegerField()),
                ('max', models.IntegerField()),
                ('warn', models.IntegerField()),
                ('inact', models.IntegerField()),
                ('expire', models.IntegerField()),
                ('flags', models.IntegerField()),
            ],
            options={
                'db_table': 'shadow',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('groupname', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('gid', models.IntegerField()),
            ],
            options={
                'db_table': 'usergroup',
                'managed': False,
            },
        ),
        migrations.AddField(
            model_name='application',
            name='md5_crypt',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='sha256_crypt',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
    ]
