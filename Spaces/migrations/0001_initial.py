# Generated by Django 3.1.2 on 2022-01-12 10:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Compound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comp_name', models.CharField(max_length=150)),
                ('comp_type', models.CharField(choices=[('F', 'flat'), ('S', 'storey building'), ('B', 'Boys Quater')], max_length=150)),
                ('noOfTenantsPerBath', models.IntegerField()),
                ('noOfTenantsPerToilet', models.IntegerField()),
                ('mapCoordinate', models.IntegerField(null=True)),
                ('areaLocated', models.CharField(max_length=500)),
                ('distanceToSchoolGate', models.DecimalField(decimal_places=1, max_digits=6)),
                ('timeOfTreckToGate', models.IntegerField()),
                ('powerSupply', models.BooleanField()),
                ('generator', models.BooleanField()),
                ('waterType', models.CharField(choices=[('B', 'borehole'), ('W', 'well')], max_length=200)),
                ('garage', models.BooleanField()),
                ('washingMachine', models.BooleanField()),
                ('swimmingPool', models.BooleanField()),
                ('smoking', models.BooleanField()),
                ('animals', models.BooleanField()),
                ('children', models.BooleanField()),
                ('partying', models.BooleanField()),
                ('check_in', models.TimeField(null=True)),
                ('check_out', models.TimeField(null=True)),
                ('extraRules', models.TextField(max_length=1000)),
                ('agentComment', models.CharField(max_length=1000)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('last_edited', models.DateTimeField(auto_now=True)),
                ('agent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ImagesTb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_type', models.CharField(max_length=50)),
                ('noOfTenantPermitted', models.IntegerField(null=True)),
                ('noOfWindows', models.IntegerField()),
                ('roomSize', models.DecimalField(decimal_places=3, max_digits=5)),
                ('airCondition', models.BooleanField()),
                ('kitchen', models.BooleanField()),
                ('flatscreenTV', models.BooleanField()),
                ('room_yearlyPrice', models.DecimalField(decimal_places=3, max_digits=10)),
                ('discount', models.DecimalField(decimal_places=3, max_digits=10)),
                ('inspection_price', models.DecimalField(decimal_places=3, max_digits=10)),
                ('wardrobe', models.BooleanField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('last_edited', models.DateTimeField(auto_now=True)),
                ('compoundId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Spaces.compound')),
            ],
        ),
        migrations.CreateModel(
            name='BookmarkTb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Spaces.room')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Inspection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Spaces.room')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('roomId', 'userId')},
            },
        ),
    ]
