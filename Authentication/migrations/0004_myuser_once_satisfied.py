# Generated by Django 4.0.2 on 2022-02-22 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0003_auto_20220129_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='once_satisfied',
            field=models.BooleanField(default=False),
        ),
    ]