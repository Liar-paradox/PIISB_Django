# Generated by Django 4.1.3 on 2023-01-13 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocenafilmow', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ocena',
            name='wartosc',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]