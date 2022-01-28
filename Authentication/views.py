from django.core.checks import messages
from Authentication.models import MyUser, VerificationCode
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import CreateUserSerializer
import random
from django.core.mail import send_mail

class CreateUser(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        reg_serializer = CreateUserSerializer(data=request.data)
        if reg_serializer.is_valid(raise_exception=True):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
            newuser = reg_serializer.save()
            if newuser:
                return Response(status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors)

class ResetCode(APIView):
    permission_classes = [AllowAny]

    def post(self, request, code_or_reset=None):
        if code_or_reset == "reset":
            user = MyUser.objects.get(email=request.data['email'])
            codeB = VerificationCode.objects.get(userId=user.id, codeType="reset")
            if codeB.code == request.data['code']:
                reg_serializer = CreateUserSerializer(user, data=request.data, partial=True)
                if reg_serializer.is_valid(raise_exception=True):
                    newuser = reg_serializer.save()
                    codeB.delete()
                    if newuser:
                        return Response(status=status.HTTP_201_CREATED)
                return Response(reg_serializer.errors)
            return  Response(status=status.HTTP_400_BAD_REQUEST, data={"message":"this is not the right code"})
        elif code_or_reset == "code":
            email = request.data["email"]
            try:
                user = MyUser.objects.get(email=email)
            except: user = ''
            if user:
                try:
                    verify = VerificationCode.objects.get(userId=user.id, codeType='Reset')
                except: verify = ""
                if verify: verify.delete()
                generated_value = random.randrange(1000, 10000)
                keepValue = VerificationCode.objects.get_or_create(codeType='Reset', code=generated_value, userId=user)
                send_mail(
                    'Password Reset',
                    f'Hello, {user.first_name}. This is your password reset code {generated_value}.\
                        Enter this into the field provided and set a new password',
                    'admin@admin.com',
                    [email],
                    fail_silently=False,
                )
                return Response(status=status.HTTP_202_ACCEPTED)
            return Response(status=status.HTTP_400_BAD_REQUEST)