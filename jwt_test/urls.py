"""jwt_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from rest_framework_jwt.views import obtain_jwt_token

# 配置drf自动接口文档 pip install coreapi
from rest_framework.documentation import include_docs_urls

from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title='站点页面标题')),

    path('login/', obtain_jwt_token),
    path('books/', views.BookView.as_view()),
    path('userinfo/', views.UserInfoAPIView.as_view()),
    path('goods/', views.GoodsInfoAPIView.as_view()),
    path('login2/', views.Login2View.as_view({'post': 'login'})),
    # path('login2/', views.Login2View.as_view()),

]
