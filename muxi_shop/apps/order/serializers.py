from rest_framework import serializers

from apps.order.models import OrderGoods
from muxi_shop.settings import IMAGE_URL


# from muxi_shop_api2.settings import IMAGE_URL


class OrderGoodsSerializer(serializers.ModelSerializer):


    class Meta:
        model = OrderGoods
        fields = "__all__"