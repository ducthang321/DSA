# Generated by Django 4.1.3 on 2022-11-29 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactform',
            old_name='uername',
            new_name='username',
        ),
        migrations.AlterField(
            model_name='contactform',
            name='body',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]
