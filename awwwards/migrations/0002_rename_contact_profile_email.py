# Generated by Django 4.0.5 on 2022-06-11 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awwwards', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='contact',
            new_name='email',
        ),
    ]
