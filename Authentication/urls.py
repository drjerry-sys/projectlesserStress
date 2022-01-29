from django.urls import path
from Authentication.views import BlacklistTokenView, CreateUser, ResetCode
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView
)

urlpatterns = [
    path('api/token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path('reset_password/<str:code_or_reset>', ResetCode.as_view(), name='reset_passord'),
    path('api/token/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('register/', CreateUser.as_view(), name='create_user'),
    path('logout/', BlacklistTokenView.as_view(), name='blacklist')
]