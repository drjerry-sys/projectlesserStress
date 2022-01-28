import time
from Spaces.models import Compound
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser, FileUploadParser
from .serializers import CompImagesSerializer, CompoundSerializer, RoomImagesSerializer, RoomSerializer

# Create your views here.

class CompoundView(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        comp_serializer = CompoundSerializer(data=request.data)
        if comp_serializer.is_valid(raise_exception=True):
            new_comp = comp_serializer.save()
            if new_comp:
                return Response(status=status.HTTP_201_CREATED)
        return Response(comp_serializer.errors)

class RoomView(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        data = request.data
        if data['compoundId'] == 0.1:
            time.sleep(3)
            belong_to = Compound.objects.filter(agent=data['agent']).order_by('-id')[0]
            data['compoundId'] = belong_to.id
        room_serializer = RoomSerializer(data=data)
        if room_serializer.is_valid(raise_exception=True):
            new_room = room_serializer.save()
            if new_room:
                return Response(status=status.HTTP_201_CREATED)
        return Response(room_serializer.error)
        

def room_helper(image):
    # webp_format = 
    to_save = {}
    to_save['room_image'] = image
    return to_save
class RoomImagesViews(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        images = dict((request.data.lists()))['room_image']
        print(images)
        # flag = 1
        # arr = []
        # for img in images:
        #     print(dict(request.data.lists()))
        #     modified = room_helper(img)
        #     img_serializer = RoomImagesSerializer(data=modified)
        #     print('this is room image serializer', img_serializer)
        #     if img_serializer.is_valid():
        #         img_serializer.save()
        #         arr.append(img_serializer.data)
        #     else:
        #         # arr.append(img_serializer.error)
        #         flag = 0
        # if flag:
        img_serializer = RoomImagesSerializer(data=request.data['comp_image'], many=True)
        print('this is room image serializer', img_serializer)
        if img_serializer.is_valid():
            img_serializer.save()
            return Response(img_serializer.data, status=status.HTTP_200_OK)
        return Response(img_serializer.error, status=status.HTTP_400_BAD_REQUEST)

def helper(compoundId, image):
    # webp_format = 
    to_save = {}
    to_save['compoundId'] = compoundId
    to_save['comp_image'] = image
    return to_save

class CompoundImagesViews(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser, JSONParser, FileUploadParser]

    def post(self, request, format=None):
        print(request.FILES)
        compoundId = request.data['compoundId']
        print('this is compound images view')
        images = dict((request.data.lists()))['comp_image']
        print(images)
        flag = 1
        arr = []
        for img in images[0]:
            print(dict(request.data.lists()))
            modified = helper(compoundId, img)
            img_serializer = CompImagesSerializer(data=modified)
            if img_serializer.is_valid():
                img_serializer.save()
                arr.append(img_serializer.data)
            else:
                # arr.append(img_serializer.error)
                flag = 0
        if flag:
            return Response(arr, status=status.HTTP_200_OK)
        return Response(arr, status=status.HTTP_400_BAD_REQUEST)