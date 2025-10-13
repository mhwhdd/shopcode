from rest_framework import serializers

from apps.address.models import UserAddress
from muxi_shop.settings import IMAGE_URL


# from muxi_shop_api2.settings import IMAGE_URL


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = "__all__"