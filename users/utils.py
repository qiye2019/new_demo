# 自定义给前端返回的内容
def my_jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'username': user.username,
        'msg': '登录成功',
        'status': 100
    }


from rest_framework.authentication import BaseAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication  # 跟上面是一个 是上面的父类
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_jwt.authentication import jwt_decode_handler  # 取出payload
from rest_framework_jwt.utils import jwt_decode_handler  # 跟上面是一个  是更深层次的底层代码
import jwt


class MyJwtAuthentication(BaseAuthentication):
    def authenticate(self, request):
        jwt_value = request.META.get('HTTP_AUTHORIZATION')
        if jwt_value:
            try:
                # 取出payload （验证信息是否正确）并提供校验功能
                payload = jwt_decode_handler(jwt_value)
            # 细化 异常类型
            except jwt.ExpiredSignature:
                raise AuthenticationFailed('签名过期')
            except jwt.InvalidTokenError:
                raise AuthenticationFailed('用户非法')
            except Exception as e:
                # 所有的异常都会走到这
                raise AuthenticationFailed(str(e))
            # 取出payload中的用户user信息
            return payload, jwt_value
        # 没有jwt_value 直接抛出一场
        raise AuthenticationFailed('您没有携带认证信息')
