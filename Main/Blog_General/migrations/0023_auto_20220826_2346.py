# Generated by Django 3.2.8 on 2022-08-27 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog_General', '0022_auto_20220826_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='muestra_inferior',
            field=models.CharField(choices=[('no', 'no'), ('si', 'si')], default='no', max_length=10),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='muestra_superior',
            field=models.CharField(choices=[('no', 'no'), ('si', 'si')], default='no', max_length=10),
        ),
    ]
