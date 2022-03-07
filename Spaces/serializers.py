from django.db.models import fields
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from .models import Compound, CompoundImages, Room, RoomImages
from Authentication.models import MyUser


class CompImagesSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField('get_image_url')
    class Meta:
        model = CompoundImages
        fields = ('image_url', 'compoundId')

    def get_image_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.room_image.url)

class RoomImagesSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField('get_image_url')
    class Meta:
        model = RoomImages
        fields = ('image_url',)

    def get_image_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.room_image.url)

class CompoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compound
        fields = '__all__'

    # def create(self, validated_data):
    #     agentId = validated_data.pop('agent', None)
    #     instance = self.Meta.model(**validated_data)
    #     if agentId is not None:
    #         instance.agent_id = agentId
    #     instance.save()
    #     return instance

class RoomSerializer(serializers.ModelSerializer):
    belong_to = CompoundSerializer(read_only=True, many=True)
    class Meta:
        model = Room
        fields = '__all__'

    # def create(self, validated_data):
    #     """for newly created compounds, compoundId is 0.1,
    #      then we select the last compound inserted by the agent
    #      Note that, the compound endpoint must be called first before this room endpoint
    #      """
    #     agentId = validated_data.pop('agent', None)
    #     compoundId = validated_data.pop('compoundId', None)
    #     instance = self.Meta.model(**validated_data)
    #     if agentId is not None:
    #         if compoundId == 0.1:
    #             belong_to = Compound.objects.filter(agent=agentId).order_by('-id')[0]
    #         else:
    #             belong_to = compoundId
    #         instance.compoundId = belong_to
    #     instance.save()
    #     return instance

class SearchSerializer(serializers.Serializer):
    kitchen = serializers.BooleanField()
    airCondition = serializers.BooleanField()
    flatscreenTV = serializers.BooleanField()
    wardrobe = serializers.BooleanField()
    roomType = serializers.CharField(max_length=50)
    cleaner = serializers.BooleanField(default=False)
    noOfWindows = serializers.IntegerField()
    bathtube = serializers.BooleanField()
    roomAreaUnit = serializers.CharField(max_length=50)
    last_edited = serializers.DateTimeField()
    noOfTenantPermitted = serializers.IntegerField()
    date_added = serializers.DateTimeField()
    taken = serializers.CharField(max_length=50, default=False)
    discount = serializers.DecimalField(decimal_places=3, max_digits=10,)
    roomArea = serializers.DecimalField(decimal_places=3, max_digits=10)
    room_yearlyPrice = serializers.DecimalField(decimal_places=7, max_digits=50)
    inspection_price = serializers.DecimalField(decimal_places=7, max_digits=50)
    # compoundId = serializers.IntegerField()
    image_url = serializers.ImageField()
    compoundId__comp_name = serializers.CharField(max_length=150)
    compoundId__latitude = serializers.DecimalField(max_digits=8, decimal_places=4)
    compoundId__longitude = serializers.DecimalField(max_digits=8, decimal_places=4)
    compoundId__areaLocated = serializers.CharField(max_length=500)