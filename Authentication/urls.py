from django.urls import path
from Authentication.views import CreateUser, ResetCode
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path('register/', CreateUser.as_view(), name='create_user'),
    path('reset_password/<str:code_or_reset>', ResetCode.as_view(), name='reset_passord')
]