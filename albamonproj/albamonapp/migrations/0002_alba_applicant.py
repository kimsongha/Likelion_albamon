# Generated by Django 3.2.3 on 2021-05-20 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albamonapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alba',
            name='applicant',
            field=models.IntegerField(default=0),
        ),
    ]
