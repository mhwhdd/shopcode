# pip install pyjwt
# 直接使用django中的key当做盐
import datetime

import jwt
from rest_framework.authentication import BaseAuthentication

from muxi_shop.settings import SECRET_KEY

# 创建一个token
def create_token(payload,timeout=1):
    headers = {
              "alg": "HS256",
              "typ": "JWT"
            }
    payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(minutes=timeout)
    result = jwt.encode(headers=headers, payload=payload, key=SECRET_KEY, algorithm='HS256')
    return result
def get_payload(token):
    result = {
        "status":False,
        "data":None,
        "error":''
    }
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        result['status'] = True
        result['data'] = payload
    except jwt.exceptions.DecodeError:
        # print("token验证失败了")
        result['error'] = "token验证失败了"
    except jwt.exceptions.ExpiredSignatureError:
        # print("token已经失效了")
        result['error'] = "token已经失效了"
    except jwt.exceptions.InvalidTokenError:
        # print("无效的、非法的token")
        result['error'] = "无效的、非法的token"
    return result


# 用户在url中进行token的参数配置
class JwtQueryParamAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.GET.get('token')
        result_payload = get_payload(token)
        print(result_payload)
        # if not result_payload['status']:
        return (result_payload, token)

# 用户在Header中进行token的参数配置
class JwtHeaderAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # 从头信息中拿到token
        # print(request.META)
        # token = request.META.get("HTTP_TOKEN")  postman中这样获取
        token = request.META.get("HTTP_AUTHORIZATION")  # 谷歌浏览器中这样获取
        # print("3333{}".format(token))
        result_payload = get_payload(token)
        # print(result_payload)
        return (result_payload,token)
