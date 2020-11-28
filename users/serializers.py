from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from users import models
from users.models import User

from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class LoginModelSerializer(serializers.ModelSerializer):
    # 登录请求，走的是post方法，默认post方法完成的是create入库校验，所以唯一约束的字段，会进行数据库唯一校验，导致逻辑相悖
    # 需要覆盖系统字段，自定义校验规则，就可以避免完成多余的不必要校验，如唯一字段校验
    username = serializers.CharField()

    class Meta:
        model = User
        # 结合前台登录布局：采用账号密码登录，或手机密码登录，布局一致，所以不管账号还是手机号，都用username字段提交的
        fields = ['username', 'password']

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        import re
        if re.match(r'^1[3-9][0-9]{9}$', username):
            # 手机号登录
            user = models.User.objects.filter(mobile=username, is_active=True).first()
        elif re.match(r'^.+@.+$', username):
            # 邮箱登录
            user = models.User.objects.filter(email=username, is_active=True).first()
        else:
            # 账号登录
            user = models.User.objects.filter(username=username, is_active=True).first()
        if user:  # 用户存在
            # 校验密码 密文，check_password
            if user.check_password(password):
                # 密码正确 签发token
                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
                self.context['token'] = token
                self.context['username']=username

                return attrs
            else:
                raise ValidationError('密码错误')

        raise ValidationError('用户不存在')
