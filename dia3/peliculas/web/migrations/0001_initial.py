# Generated by Django 4.2 on 2024-02-23 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('imagen', models.CharField(max_length=255)),
                ('puntaje', models.IntegerField()),
            ],
        ),
    ]
