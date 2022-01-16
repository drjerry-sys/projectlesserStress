from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import CompImagesSerializer, CompoundSerializer, RoomImagesSerializer, RoomSerializer

# Create your views here.

class CompoundView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        comp_serializer = CompoundSerializer(data=request.data)
        if comp_serializer.is_valid(raise_exception=True):
            new_comp = comp_serializer.save()
            if new_comp:
                return Response(status=status.HTTP_201_CREATED)
        return Response(comp_serializer.errors)

class RoomView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):        
        room_serializer = RoomSerializer(data=request.data)
        if room_serializer.is_valid(raise_exception=True):
            new_room = room_serializer.save()
            if new_room:
                return Response(status=status.HTTP_201_CREATED)
        return Response(room_serializer.error)
        
class RoomImagesViews(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        img_serializer = RoomImagesSerializer(data=request.data)
        if img_serializer.is_valid(raise_exception=True):
            img_serializer.save()
            return Response(img_serializer.data, status=status.HTTP_200_OK)
        return Response(img_serializer.error, status=status.HTTP_400_BAD_REQUEST)

def helper(compoundId, image):
    to_save = {}
    to_save['compoundId'] = compoundId
    to_save['image'] = image
    return to_save

class CompoundImagesViews(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        compoundId = request.data['compoundId']
        images = dict((request.data.lists()))['image']
        flag = 1
        arr = []
        for img in images:
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