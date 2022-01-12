from django.db import models
from Authentication.models import MyUser

# Create your models here.
class Compound(models.Model):
    water = (
        ('B', 'borehole'),
        ('W', 'well')
    )
    comp_name = models.CharField(max_length=150)
    comp_type = models.CharField(max_length=150, null=False, blank=False)
    noOfTenantsPerBath = models.IntegerField(null=False)
    noOfTenantsPerToilet = models.IntegerField(null=False)
    mapCoordinate = models.IntegerField(null=True)
    areaLocated = models.CharField(max_length=500)
    distanceToSchoolGate = models.DecimalField(decimal_places=1, max_digits=6)
    timeOfTreckToGate = models.IntegerField()
    powerSupply = models.BooleanField()
    generator = models.BooleanField()
    waterType = models.CharField(max_length=200, choices=water)
    garage = models.BooleanField()
    washingMachine = models.BooleanField()
    swimmingPool = models.BooleanField()
    smoking = models.BooleanField()
    animals = models.BooleanField()
    children = models.BooleanField()
    partying = models.BooleanField()
    check_in = models.TimeField(null=True)
    check_out = models.TimeField(null=True)
    extraRules = models.TextField(max_length=1000)
    agentComment = models.CharField(max_length=1000)
    date_added = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)
    latitude = models.DecimalField(decimal_places=8, max_digits=8)
    longitude = models.DecimalField(decimal_places=8, max_digits=8)
    agent_id = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.comp_name} added'

class Room(models.Model):
    choices = (
        ('S', 'single room'),
        ('SC', 'self contained'),
    )
    room_type = models.CharField(max_length=50)
    noOfTenantPermitted = models.IntegerField(null=True)
    noOfWindows = models.IntegerField(null=False)
    roomSize = models.DecimalField(decimal_places=3, max_digits=5)
    airCondition = models.BooleanField()
    kitchen = models.BooleanField()
    flatscreenTV = models.BooleanField()
    room_yearlyPrice = models.DecimalField(decimal_places=3, max_digits=10)
    discount = models.DecimalField(decimal_places=3, max_digits=10)
    inspection_price = models.DecimalField(decimal_places=3, max_digits=10)
    wardrobe = models.BooleanField()
    date_added = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)
    compoundId = models.ForeignKey(Compound, unique=False, on_delete=models.CASCADE)

class ImagesTb(models.Model):
    pass

class BookmarkTb(models.Model):
    userId = models.ForeignKey(MyUser, unique=False, on_delete=models.CASCADE)
    roomId = models.ForeignKey(Room, unique=False, on_delete=models.CASCADE)

class Inspection(models.Model):
    roomId = models.ForeignKey(Room, on_delete=models.CASCADE)
    userId = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('roomId', 'userId')