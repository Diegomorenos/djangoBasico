# Generated by Django 4.2.6 on 2023-10-23 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoteleria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('hab_numero', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('hab_estado', models.CharField(max_length=7, null=True)),
                ('tipo_hab_id', models.CharField(max_length=7, null=True)),
                ('hab_tarifa', models.CharField(max_length=7, null=True)),
                ('hab_capacidad', models.CharField(max_length=7, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
