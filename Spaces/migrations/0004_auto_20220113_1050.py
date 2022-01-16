# Generated by Django 3.1.2 on 2022-01-13 09:50

import Spaces.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Spaces', '0003_auto_20220112_1623'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='inspection',
            unique_together=set(),
        ),
        migrations.CreateModel(
            name='RoomImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='room/default.jpg', upload_to=Spaces.models.uploadroom_to, verbose_name='Image')),
                ('compoundId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Spaces.compound')),
            ],
        ),
        migrations.CreateModel(
            name='CompoundImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='compound/default.jpg', upload_to=Spaces.models.upload_to, verbose_name='Image')),
                ('compoundId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Spaces.compound')),
            ],
        ),
    ]
