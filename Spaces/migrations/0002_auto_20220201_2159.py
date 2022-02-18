# Generated by Django 3.1.2 on 2022-02-01 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Spaces', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compoundimages',
            name='compoundId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='compound_images', to='Spaces.compound'),
        ),
        migrations.AlterField(
            model_name='roomimages',
            name='roomId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_images', to='Spaces.room'),
        ),
    ]
