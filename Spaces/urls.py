from django.urls import path

from Spaces.views import CompoundImagesViews, CompoundView, RoomImagesViews, RoomView

urlpatterns = [
    path('room/images/', RoomImagesViews.as_view(), name='roomimg'),
    path('compound/images/', CompoundImagesViews.as_view(), name='compoundimg'),
    path('compound/', CompoundView.as_view(), name='compound'),
    path('room/', RoomView.as_view(), name='room'),
]