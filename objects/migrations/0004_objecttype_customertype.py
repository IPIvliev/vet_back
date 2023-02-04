# Generated by Django 4.0.4 on 2023-01-18 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0003_object_object_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ObjectType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=160, verbose_name='Тип объекта')),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='objects.object')),
            ],
            options={
                'verbose_name': 'Тип объектов',
                'verbose_name_plural': 'Типы объектов',
            },
        ),
        migrations.CreateModel(
            name='CustomerType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=160, verbose_name='Тип потребилетя')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='objects.customer')),
            ],
            options={
                'verbose_name': 'Тип потребитей',
                'verbose_name_plural': 'Типы потребителей',
            },
        ),
    ]