# Generated by Django 2.2.5 on 2019-11-19 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateTimeField(blank=True, null=True, default=None, verbose_name='Date'),
            preserve_default=False,
        ),
    ]
