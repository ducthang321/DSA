# Generated by Django 4.1.3 on 2022-12-05 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='core',
            name='SSN',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='core',
            name='birthday',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='core',
            name='firstname',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='core',
            name='lastname',
            field=models.TextField(max_length=255),
        ),
    ]
