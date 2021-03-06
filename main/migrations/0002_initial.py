# Generated by Django 4.0.2 on 2022-02-16 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='meal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='menu.meal'),
        ),
        migrations.AddField(
            model_name='order',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.restaurant'),
        ),
    ]
