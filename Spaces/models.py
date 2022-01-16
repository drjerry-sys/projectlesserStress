from django.db import models
from Authentication.models import MyUser
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Compound(models.Model):
    water = (
        ('B', 'borehole'),
        ('W', 'well')
    )
    comp_name = models.CharField(max_length=150)
    comp_type = models.CharField(max_length=150, null=False, blank=False)
    noOfRoomsPerBath = models.IntegerField(null=False)
    noOfRoomsPerToilet = models.IntegerField(null=False)
    areaLocated = models.CharField(max_length=500)
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
    distanceToSchoolGate = models.DecimalField(decimal_places=1, max_digits=6)
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
    roomAreaUnit = models.CharField(max_length=50)
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


class BookmarkTb(models.Model):
    userId = models.ForeignKey(MyUser, unique=False, on_delete=models.CASCADE)
    roomId = models.ForeignKey(Room, unique=False, on_delete=models.CASCADE)

class Inspection(models.Model):
    roomId = models.ForeignKey(Room, on_delete=models.CASCADE)
    userId = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    # class Meta:
    #     unique_together = ('roomId', 'userId')
def upload_to(instance, filename):
    return f'compound/{filename}'

def uploadroom_to(instance, filename):
    return f'room/{filename}'

class CompoundImages(models.Model):
    compoundId = models.ForeignKey(Compound, on_delete=models.CASCADE)
    image = models.ImageField(_('Image'), upload_to=upload_to, default='compound/default.jpg')

class RoomImages(models.Model):
    roomId = models.ForeignKey(Room, on_delete=models.CASCADE)
    image = models.ImageField(_('Image'), upload_to=uploadroom_to, default='room/default.jpg')