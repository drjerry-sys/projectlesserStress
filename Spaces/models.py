from django.db import models
from Authentication.models import MyUser
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Compound(models.Model):
    water = (
        ('B', 'borehole'),
        ('W', 'well')
    )
    garage = models.BooleanField()
    smoking = models.BooleanField()
    animals = models.BooleanField()
    children = models.BooleanField()
    borehole = models.BooleanField()
    partying = models.BooleanField()
    wellWater = models.BooleanField()
    generator = models.BooleanField()
    powerSupply = models.BooleanField()
    swimmingPool = models.BooleanField()
    washingMachine = models.BooleanField()
    check_in = models.TimeField(null=True)
    check_out = models.TimeField(null=True)
    noOfRoomsPerBath = models.IntegerField()
    noOfRoomsPerToilet = models.IntegerField()
    ownerType = models.CharField(max_length=150)
    areaLocated = models.CharField(max_length=500)
    last_edited = models.DateTimeField(auto_now=True)
    timeOfTreckToGate = models.IntegerField(default=323)
    date_added = models.DateTimeField(auto_now_add=True)
    comp_name = models.CharField(max_length=150, null=True)
    comp_type = models.CharField(max_length=150, blank=False)
    address = models.CharField(max_length=150, blank=False, null=True)
    extraRules = models.TextField(max_length=1000, null=True)
    agentComment = models.CharField(max_length=1000, null=True)
    agent = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=8, decimal_places=4, default=3233.434)
    longitude = models.DecimalField(max_digits=8, decimal_places=4, default=32423.343)
    distanceToSchoolGate = models.DecimalField(max_digits=6, decimal_places=1, default=3233.4)

    class Meta:
        unique_together = ('comp_name', 'id')

    def __str__(self) -> str:
        return f'{self.comp_name} added'

class Room(models.Model):
    kitchen = models.BooleanField()
    airCondition = models.BooleanField()
    flatscreenTV = models.BooleanField()
    wardrobe = models.BooleanField(null=True)
    roomType = models.CharField(max_length=50)
    cleaner = models.BooleanField(default=False)
    noOfWindows = models.IntegerField(null=False)
    bathtube = models.BooleanField(default=False)
    roomAreaUnit = models.CharField(max_length=50)
    last_edited = models.DateTimeField(auto_now=True)
    noOfTenantPermitted = models.IntegerField(null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    taken = models.CharField(max_length=50, default=False)
    discount = models.DecimalField(decimal_places=3, max_digits=10, null=True)
    roomArea = models.DecimalField(decimal_places=3, max_digits=10, null=True)
    room_yearlyPrice = models.DecimalField(decimal_places=7, max_digits=50, null=True)
    inspection_price = models.DecimalField(decimal_places=7, max_digits=50, null=True)
    compoundId = models.ForeignKey(Compound, related_name='belong_to', unique=False, on_delete=models.CASCADE, null=True)
    
class BookmarkTb(models.Model):
    roomId = models.ForeignKey(Room, unique=False, on_delete=models.CASCADE)
    userId = models.ForeignKey(MyUser, unique=False, on_delete=models.CASCADE)

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
    compoundId = models.ForeignKey(Compound, on_delete=models.CASCADE, related_name='compound_images', null=True)
    comp_image = models.ImageField(_('Image'), upload_to=upload_to, default='compound/default.jpg')

class RoomImages(models.Model):
    roomId = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_images')
    room_image = models.ImageField(_('Image'), upload_to=uploadroom_to, default='room/default.jpg')