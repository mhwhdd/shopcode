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
        print("token验证失败了")
        result['error'] = "token验证失败了"
    except jwt.exceptions.ExpiredSignatureError:
        print("token已经失效了")
        result['error'] = "token已经失效了"
    except jwt.exceptions.InvalidTokenError:
        print("无效的、非法的token")
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

