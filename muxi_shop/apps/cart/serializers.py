from rest_framework import serializers
from apps.cart.models import ShoppingCart
class CartsSerializer(serializers.ModelSerializer):
    # 这里边写的字段就是你想要进行序列化时处理的字段
    sku_id = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    class Meta:
        model = ShoppingCart
        fields = "__all__"