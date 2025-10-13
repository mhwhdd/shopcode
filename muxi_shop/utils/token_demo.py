# pip install pyjwt
# 直接使用django中的key当做盐
import datetime

import jwt

from muxi_shop.settings import SECRET_KEY

# 创建一个token
def create_token():
    headers = {
              "alg": "HS256",
              "typ": "JWT"
            }
    payload = {
        'user_id':1,
        'user_name':'mhw',
        'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=0.1)#超时时间
    }
    result = jwt.encode(headers=headers, payload=payload, key=SECRET_KEY, algorithm='HS256')
    return result
def get_payload(token):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    except jwt.exceptions.DecodeError:
        print("token验证失败了")
    except jwt.exceptions.ExpiredSignatureError:
        print("token已经失效了")


   # return jwt.decode(token, key=SECRET_KEY, algorithms=['HS256'])
if __name__ == '__main__':
    # token = create_token()
    token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJ1c2VyX25hbWUiOiJtaHciLCJleHAiOjE3NjAzNDcxMjd9.PtbeNE9c3RjjzypUvvD0LXS0Pi0Hd5t9-7ucNnuS99s'
    print("============{}".format(token))
    payload = get_payload(token)
    print(payload)
