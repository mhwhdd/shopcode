from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView

from apps.cart.models import ShoppingCart
from apps.cart.serializers import CartsSerializer
from utils import ResponseMessage


# Create your views here.
class CartAPIView(APIView):
    # 我们的购物车应该是登录后才能使用
    # @todo 后续补充登录权限验证
    def post(self, request):
        request_data = request.data
        # print("request_data==={}".format(request_data))
        # print(type(request_data))
        email = request_data.get('email')
        # print("email={}".format(email))
        sku_id = request_data.get('sku_id')
        nums = request_data.get('nums')
        is_delete = request_data.get('is_delete')
        # 判断一下数据是否存在，如果存在就更新，如果不存在就插入
        data_exists = ShoppingCart.objects.filter(email=email,is_delete=0, sku_id=sku_id)
        # print("yy==={}".format(data_exists))
        # 存在就更新
        if data_exists.exists():
            # print("qqqqqq=={}".format(data_exists))
            exists_cart_data = data_exists.get(email=email, is_delete=0, sku_id=sku_id)
            if is_delete == 0:
                new_nums = exists_cart_data.nums + nums
                request_data['is_delete'] = 0
                request_data['nums'] = new_nums
            elif is_delete == 1:
                exists_cart_data.nums = exists_cart_data.nums
            # 反序列化
            cart_ser =  CartsSerializer(data=request_data)
            cart_ser.is_valid(raise_exception=True)
            # print("插入======{}".format(cart_ser))
            # 更新
            ShoppingCart.objects.filter(email=email, is_delete=0, sku_id=sku_id).update(**cart_ser.data)
            if is_delete == 0:
                return ResponseMessage.CartResponse.success("更新成功")
            elif is_delete == 1:
                return ResponseMessage.CartResponse.success("删除成功")


        else:
            request_data['is_delete'] = 0
            cart_ser = CartsSerializer(data=request_data)
            # print("======{}".format(cart_ser))
            cart_ser.is_valid(raise_exception=True)
            # 插入数据
            ShoppingCart.objects.create(**cart_ser.data)
            return ResponseMessage.CartResponse.success("插入成功")
            return HttpResponse("插入成功")
    def get(self,request):
        email = request.GET.get('email')
        cart_result = ShoppingCart.objects.filter(email=email, is_delete=0)
        cart_ser = CartsSerializer(instance=cart_result, many=True)
        return ResponseMessage.CartResponse.success(cart_ser.data)