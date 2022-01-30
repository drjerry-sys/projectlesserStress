from django.urls import path
from .views import homeRoomsViews
from Spaces.views import CompoundImagesViews, CompoundView, RoomImagesViews, RoomView

urlpatterns = [
    path('room/images/', RoomImagesViews.as_view(), name='roomimg'),
    path('compound/images/', CompoundImagesViews.as_view(), name='compoundimg'),
    path('compound/', CompoundView.as_view(), name='compound'),
    path('room/', RoomView.as_view(), name='room'),
    path('home-rooms/', homeRoomsViews, name='home_rooms')
]