# Generated by Django 2.2.5 on 2019-09-18 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sassyi_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scan',
            name='scan_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
