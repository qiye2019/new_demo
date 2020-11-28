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

    # permission_classes = [IsAuthenticated, ]

    def get(self, request):
        print(request.user)
        return Response('ok')


class UserInfoAPIView(APIView):
    # authentication_classes = [JSONWebTokenAuthentication,]

    permission_classes = [IsAuthenticated, ]
    def get(self, request):
        return Response('OK')


from users.utils import MyJwtAuthentication


class GoodsInfoAPIView(APIView):
    authentication_classes = [MyJwtAuthentication, ]

    # 权限控制
    # permission_classes = [IsAuthenticated,]

    def get(self, request, *args, **kwargs):
        print(request.user)
        return Response('商品信息')


# 多账户登录接口
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin, ViewSet
from users.serializers import LoginModelSerializer


class Login2View(ViewSet):  # ViewSet继承自 ViewSetMixin，APIView
    # def post(self):
    # 这是登录接口
    # pass
    authentication_classes = [MyJwtAuthentication, ]

    # 自定义login 实现多方式登录
    def login(self, request, *args, **kwargs):
        # 1 序列化类
        login_serializers = LoginModelSerializer(data=request.data, context={'request': request})
        # 2 生成序列化类对象
        # 3 调用序列化对象的is_valid
        login_serializers.is_valid(raise_exception=True)
        token = login_serializers.context.get('token')

        username = login_serializers.context.get('username')

        return Response(
            {'status': 100, 'msg': '登录成功', 'token': token, 'username': username})
