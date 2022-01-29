from django.db.models import fields
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from .models import Compound, CompoundImages, Room, RoomImages
from Authentication.models import MyUser

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = (
            'roomType', 'noOfTenantPermitted', 'noOfWindows', 'roomArea', 'airCondition', 'kitchen', 'flatscreenTV',
            'room_yearlyPrice', 'discount', 'inspection_price', 'wardrobe', 'date_added', 'last_edited', 'compoundId'
        )

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

class CompoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compound
        fields = (
            'comp_name', 'comp_type', 'noOfRoomsPerBath', 'noOfRoomsPerToilet', 'areaLocated', 'distanceToSchoolGate',
            'longitude', 'latitude', 'last_edited', 'date_added', 'agentComment', 'extraRules', 'check_out', 'check_in',
            'partying', 'children', 'animals', 'smoking', 'swimmingPool', 'washingMachine', 'garage', 'wellWater', 'borehole', 'generator',
            'powerSupply', 'timeOfTreckToGate', 'agent'
        )

    # def create(self, validated_data):
    #     agentId = validated_data.pop('agent', None)
    #     instance = self.Meta.model(**validated_data)
    #     if agentId is not None:
    #         instance.agent_id = agentId
    #     instance.save()
    #     return instance

class CompImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompoundImages
        fields = ('comp_image', 'compoundId')

class RoomImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImages
        fields = ('room_image', 'roomId')