# Generated by Django 2.1.2 on 2018-10-14 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20181014_1447'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='vector_encoding',
        ),
        migrations.AddField(
            model_name='person',
            name='date_of_missing',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='is_missing',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='person',
            name='place_of_missing',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
