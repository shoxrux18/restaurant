# Generated by Django 4.0.2 on 2022-02-16 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='stol',
            field=models.IntegerField(default=0),
        ),
    ]
