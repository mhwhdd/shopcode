from rest_framework import serializers

from apps.comment.models import Comment
from muxi_shop.settings import IMAGE_URL


# from muxi_shop_api2.settings import IMAGE_URL


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"