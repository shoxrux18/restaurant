# Generated by Django 4.0.2 on 2022-02-16 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_restaurant_stol'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order_id',
            new_name='restaurant',
        ),
        migrations.RemoveField(
            model_name='order',
            name='meal',
        ),
        migrations.RemoveField(
            model_name='order',
            name='price',
        ),
        migrations.RemoveField(
            model_name='order',
            name='table',
        ),
        migrations.RemoveField(
            model_name='order',
            name='time',
        ),
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='number_of_table',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.IntegerField(null=True),
        ),
        migrations.CreateModel(
            name='OrderMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=50)),
                ('name_en', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.order')),
            ],
        ),
    ]
