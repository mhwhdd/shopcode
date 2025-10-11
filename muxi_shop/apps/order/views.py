from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.generics import GenericAPIView

from apps.order.models import OrderGoods,Order
from apps.order.serializers import OrderGoodsSerializer


# Create your views here.
class OrderGoodsGenericAPIView(GenericAPIView):
    queryset = OrderGoods.objects.all()
    serializer_class = OrderGoodsSerializer
    def post(self, request, *args, **kwargs):
        # trade_no = request.GET.get('trade_no')
        # print(self.get_queryset())
        # print(self.get_serializer())
        # 序列化
        ser = self.get_serializer(data=request.data)
        ser.is_valid(raise_exception=True)
        ser.save() # 创建保存到数据库 不需要写sql
        return JsonResponse({"code":200, "msg":"success"})
        self.get_queryset()
        self.get_serializer()
    lookup_field = 'trade_no'
    def get(self, request,trade_no):
        # self.get_serializer(instance=self.get_queryset(), many=True) # 完成整个查询
        # return JsonResponse(self.get_serializer(instance=self.get_queryset(), many=True).data,safe=False)
        ser = self.get_serializer(instance=self.get_object(),many=False)
        return JsonResponse(ser.data,safe=False)