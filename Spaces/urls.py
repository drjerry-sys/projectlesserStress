from django.urls import path
from .views import homeDataViews, searchResults
from django.conf import settings
from django.conf.urls.static import static
from Spaces.views import CompoundImagesViews, CompoundView, RoomImagesViews, RoomView

urlpatterns = [
    path('compound/images/', CompoundImagesViews.as_view(), name='compoundimg'),
    path('room/images/', RoomImagesViews.as_view(), name='roomimg'),
    path('compound/', CompoundView.as_view(), name='compound'),
    path('home-rooms/', homeDataViews, name='home_rooms'),
    path('room/', RoomView.as_view(), name='room'),
    path('all-searches/<str:area>/<str:price>/', searchResults, name='room'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)