from email.mime import image
from multiprocessing import context
import time
from django.db import connection
from Authentication.models import MyUser
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from .helperFunctions import helper, room_helper
from Spaces.models import Compound, CompoundImages, Room, RoomImages
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import CompImagesSerializer, CompoundSerializer, RoomImagesSerializer, RoomSerializer
# Create your views here.


cursor = connection.cursor()

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


@api_view(('GET',))
@renderer_classes((JSONRenderer, ))
def homeDataViews(request):
    if request.method == 'GET':
        user_satisfied = MyUser.objects.filter(once_satisfied=False).count()
        freeSpace = Room.objects.filter(taken=False).count()
        data = {'spaces': [], 'myName': request.user.first_name if request.user.is_authenticated else '', 'user_satisfied': user_satisfied, 'freeSpace': freeSpace}
        rooms = Room.objects.all().values()[:6]
        # this code serializes the room images and room data and appends it to the data variable
        # which is then pushed to the front-end
        for room in rooms:
            queryset = RoomImages.objects.filter(roomId = room['id'])
            rm_serializer = RoomSerializer(room)
            serializer = RoomImagesSerializer(queryset, context={'request': request}, many=True)
            data['spaces'].append({"data": rm_serializer.data,"images": serializer.data})
        return Response(data)

check = []
@api_view(('GET',))
def searchResults(request, area, price):
    data = []
    if request.method == "GET":
        start, end = price.split("-")
        start, end = int(start[1:].strip().replace(',', '').replace('₦', '')), int(end[1:].strip().replace(',', '').replace('₦', ''))
        search_result = Room.objects.select_related("compoundId").filter(room_yearlyPrice__range=(start, end))
        # search_result = Room.objects.all().select_related("compoundId")
        # print({'search_result': search_result.values()})
        # try:
        for room in search_result:
            if room.compoundId in check:
                continue
            queryset = Compound.objects.filter(id=room.compoundId)
            images = CompoundImages.objects.filter(compoundId=room.compoundId)
            comp_serializers = CompoundSerializer(queryset, many=True)
            img_serializers = CompImagesSerializer(images, many=True)
            data.append({'data': comp_serializers, 'images': img_serializers})
            check.append(room.compoundId)
        serializer = RoomSerializer(search_result, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

