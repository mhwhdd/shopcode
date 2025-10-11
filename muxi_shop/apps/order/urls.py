
from django.urls import path, re_path
from .views import OrderGoodsGenericAPIView
urlpatterns = [
    path('goods/', OrderGoodsGenericAPIView.as_view()),
    # .* 表示配置所有
    re_path("goods/(?P<trade_no>.*)", OrderGoodsGenericAPIView.as_view()),


]