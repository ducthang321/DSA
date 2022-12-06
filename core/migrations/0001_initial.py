# Generated by Django 4.1.3 on 2022-12-05 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='core',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SSN', models.CharField(max_length=25)),
                ('lastname', models.TextField(max_length=30)),
                ('firstname', models.TextField(max_length=30)),
                ('birthday', models.DateTimeField()),
                ('phone', models.IntegerField(default=0)),
                ('address', models.TextField()),
                ('company', models.TextField()),
            ],
        ),
    ]
