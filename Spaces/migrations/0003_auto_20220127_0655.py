# Generated by Django 3.1.2 on 2022-01-27 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Spaces', '0002_room_compound'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='compound',
            new_name='compoundId',
        ),
    ]
