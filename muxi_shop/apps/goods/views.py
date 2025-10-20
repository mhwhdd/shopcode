import datetime
import decimal
import json

from django.shortcuts import render
from rest_framework.views import APIView
from apps.goods.models import Goods
from apps.goods.serializers import GoodsSerializer
from utils import ResponseMessage
from django.db import  connection
from django.conf import settings
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
class GoodsSearchAPIView(APIView):
    def get(self, request,keyword,page,order_by):
        """
            # SELECT r.comment_count,g.name,g.p_price,g.shop_name,g.sku_id FROM goods g
            # LEFT JOIN
            # (SELECT count(c.sku_id) as comment_count,c.sku_id FROM comment c GROUP BY c.sku_id) r
            # on g.sku_id = r.sku_id
            # WHERE g.name LIKE "%手机%"
            # ORDER BY r.comment_count DESC LIMIT 3
        """
        order_dict = {
            1: "r.comment_count",
            2: "g.p_price"
        }

        limit_page = (page-1)*15
        # 执行原生sql
        sql = """
            select r.comment_count,concat('{}',g.image) as image,g.name,g.p_price,g.shop_name,g.sku_id from goods g
                left join
                (
                select count(c.sku_id) as comment_count,c.sku_id from comment c group by c.sku_id
                ) r
                on g.sku_id=r.sku_id
                where g.name like "%{}%"
                order by {} desc limit {},15
        """.format(settings.IMAGE_URL,keyword,order_dict[order_by],limit_page)
        cursor = connection.cursor() # 聚焦
        cursor.execute(sql) #执行
        res = self.dict_fetchall(cursor)
        final_list = []
        for i in res:
            res_json = json.dumps(i, cls=DecimalEncoder, ensure_ascii=False)
            final_list.append(res_json)
        return ResponseMessage.GoodsResponse.success(final_list)

    def dict_fetchall(self, cursor):
        desc = cursor.description
        print(desc)
        return [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        elif isinstance(o, datetime):
            return o.strftime("%Y-%m-%d %H:%M:%S")

class GoodsSearchDataCountAPIView(APIView):
    def get(self, request,sku_id):
        goods_data = Goods.objects.filter(sku_id=sku_id).all()
        print("goods_data==={}".format(goods_data))
        result = GoodsSerializer(instance=goods_data)

        return ResponseMessage.GoodsResponse.success(result.data)