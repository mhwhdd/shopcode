"""
    1000 成功
    1001 失败
    1002 其他
"""
import json

from django.http import HttpResponse, JsonResponse
class MenuResponse():

    @staticmethod
    def success(data):
        result = {"status":1000,"data":data}
        return HttpResponse(json.dumps(result), content_type = "application/json")

    @staticmethod
    def failed(data):
        result = {"status": 1001, "data": data}
        return HttpResponse(json.dumps(result), content_type="application/json")

    @staticmethod
    def other(data):
        result = {"status": 1002, "data": data}
        return HttpResponse(json.dumps(result), content_type="application/json")

class GoodsResponse():

    @staticmethod
    def success(data):
        result = {"status":2000,"data":data}
        return HttpResponse(json.dumps(result), content_type = "application/json")

    @staticmethod
    def failed(data):
        result = {"status": 2001, "data": data}
        return HttpResponse(json.dumps(result), content_type="application/json")

    @staticmethod
    def other(data):
        result = {"status": 2002, "data": data}
        return HttpResponse(json.dumps(result), content_type="application/json")

class CartResponse():

    @staticmethod
    def success(data):
        result = {"status":3000,"data":data}
        return JsonResponse(result, safe=False)

    @staticmethod
    def failed(data):
        result = {"status": 3001, "data": data}
        return JsonResponse(result, safe=False)

    @staticmethod
    def other(data):
        result = {"status": 3002, "data": data}
        return JsonResponse(result, safe=False)
# 用户返回相关
class UserResponse():

    @staticmethod
    def success(data):
        result = {"status":4000,"data":data}
        return JsonResponse(result, safe=False)

    @staticmethod
    def failed(data):
        result = {"status": 4001, "data": data}
        return JsonResponse(result, safe=False)

    @staticmethod
    def other(data):
        result = {"status": 4002, "data": data}
        return JsonResponse(result, safe=False)