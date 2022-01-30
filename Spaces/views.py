import time
from Spaces.models import Compound, Room
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import CompImagesSerializer, CompoundSerializer, RoomImagesSerializer, RoomSerializer
from .helperFunctions import helper, room_helper
# Create your views here.

class CompoundView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        my_compounds = Compound.objects.filter(agent=request.user.id)
        serializer = CompoundSerializer(my_compounds, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        val = request.data
        val['agent'] = request.user.id
        comp_serializer = CompoundSerializer(data=val)
        if comp_serializer.is_valid(raise_exception=True):
            new_comp = comp_serializer.save()
            if new_comp:
                return Response(status=status.HTTP_201_CREATED)
        return Response(comp_serializer.errors)

class RoomView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        data = request.data
        if data['compoundId'] == 0.1:
            time.sleep(1) # this timing affects the room image timing
            belong_to = Compound.objects.filter(agent=request.user.id).order_by('-id')[0]
            data['compoundId'] = belong_to.id
        room_serializer = RoomSerializer(data=data)
        if room_serializer.is_valid(raise_exception=True):
            new_room = room_serializer.save()
            if new_room:
                return Response(status=status.HTTP_201_CREATED)
        return Response(room_serializer.errors)        

class RoomImagesViews(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        print('this is user id', request.user.id)
        agent = request.user.id
        if request.data['compoundId'] == '0.1':
            compid = Compound.objects.filter(agent=int(agent)).order_by('-id')[0].id
        else:
            compid = int(request.data['compoundId'][0])
        time.sleep(2)  # take note of the timing in roomview
        roomId = Room.objects.filter(compoundId=compid).order_by('-id')[0]
        images = dict((request.data).lists())['room_image']
        flag = 1
        arr = []
        for img in images:
            modified = room_helper(roomId.id, img)
            img_serializer = RoomImagesSerializer(data=modified)
            if img_serializer.is_valid(raise_exception=True):
                img_serializer.save()
                arr.append(img_serializer.data)
            else:
                print(img_serializer.errors)
                flag = 0
        if flag:
            return Response(arr, status=status.HTTP_200_OK)
        return Response(arr, status=status.HTTP_400_BAD_REQUEST)

class CompoundImagesViews(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        compoundId = request.data['compoundId']
        agent = request.user.id
        images = dict((request.data).lists())['comp_image']
        flag = 1
        arr = []
        for img in images:
            modified = helper(compoundId, img, agent)
            img_serializer = CompImagesSerializer(data=modified)
            if img_serializer.is_valid(raise_exception=True):
                img_serializer.save()
                arr.append(img_serializer.data)
            else:
                flag = 0
        if flag:
            return Response(arr, status=status.HTTP_200_OK)
        return Response(arr, status=status.HTTP_400_BAD_REQUEST)