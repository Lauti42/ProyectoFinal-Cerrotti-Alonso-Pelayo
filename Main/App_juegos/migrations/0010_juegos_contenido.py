# Generated by Django 3.2.8 on 2022-08-22 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_juegos', '0009_auto_20220822_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='juegos',
            name='contenido',
            field=models.TextField(max_length=3000, null=True),
        ),
    ]
