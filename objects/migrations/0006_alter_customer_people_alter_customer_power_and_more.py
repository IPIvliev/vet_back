# Generated by Django 4.0.4 on 2023-01-18 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0005_remove_customertype_customer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='people',
            field=models.IntegerField(blank=True, verbose_name='Кол-во абонентов'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='power',
            field=models.FloatField(blank=True, verbose_name='Мощность'),
        ),
        migrations.AlterField(
            model_name='object',
            name='boilers',
            field=models.IntegerField(blank=True, verbose_name='Кол-во котлов'),
        ),
        migrations.AlterField(
            model_name='object',
            name='meters',
            field=models.IntegerField(blank=True, verbose_name='Площадь'),
        ),
        migrations.AlterField(
            model_name='object',
            name='people',
            field=models.IntegerField(blank=True, verbose_name='Кол-во людей'),
        ),
        migrations.AlterField(
            model_name='object',
            name='power',
            field=models.FloatField(blank=True, verbose_name='Мощность'),
        ),
        migrations.AlterField(
            model_name='object',
            name='pumps',
            field=models.IntegerField(blank=True, verbose_name='Кол-во насосов'),
        ),
    ]
