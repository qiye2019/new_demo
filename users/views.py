from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from users.my_autho import My_Token
from .models import User
from rest_framework.permissions import IsAuthenticated
class BookView(APIView):
    # authentication_classes = [My_Token, ]
    # 权限控制

    permission_classes = [IsAuthenticated,]

    def get(self, request):
        print(request.user)
        return Response('ok')

class UserInfoAPIView(APIView):
    # authentication_classes = [JSONWebTokenAuthentication.]
    # 权限控制
    # permission_classes = [IsAuthenticated,]

    def get(self,request):
        return Response('OK')
