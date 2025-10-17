from django.shortcuts import render
from rest_framework.views import APIView
from apps.goods.models import Goods
from apps.goods.serializers import GoodsSerializer
from utils import ResponseMessage
# Create your views here.
# 获取商品分类的接口
# 访问方式是: http://localhost:8000/goods/category/1

class GoodsCategoryAPIView(APIView):
    def get(self, request,category_id,page):
        current_page = (int(page) - 1)*20
        end_page = int(page)*20
        print("current_page==={}".format(current_page))
        print("category_id==={}".format(category_id))

        category_data = Goods.objects.filter(type_id=category_id).all()[current_page:end_page]
        print("category_data==={}".format(category_data))

        result_list = []
        for item in category_data:
            result_list.append(item.__str__())
        return ResponseMessage.GoodsResponse.success(result_list)

class GoodsDetailAPIView(APIView):
    def get(self, request, sku_id):
        print(sku_id)
        goods_data = Goods.objects.filter(
            sku_id=sku_id
        ).first()
        print("goods_data==={}".format(goods_data))
        # 进行序列化的动作 序列化的参数时instance， 反序列化的参数就是data
        result = GoodsSerializer(instance=goods_data)

        return ResponseMessage.GoodsResponse.success(result.data)

class GoodsFindAPIView(APIView):
    def get(self, request):
       
        goods_data = Goods.objects.filter(find=1).all()
        print("goods_data==={}".format(goods_data))
        result = GoodsSerializer(instance=goods_data,many=True)
        return ResponseMessage.GoodsResponse.success(result.data)
