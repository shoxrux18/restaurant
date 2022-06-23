# Generated by Django 4.0.2 on 2022-02-16 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=100)),
                ('name_en', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.SmallIntegerField(choices=[(1, 'Mavjud'), (0, 'Mavjudmas')])),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.restaurant')),
            ],
        ),
    ]
