
from django.urls import path
from .views import GoodsCategoryAPIView, GoodsDetailAPIView, GoodsFindAPIView

urlpatterns = [
    path("find", GoodsFindAPIView.as_view()),
    path('category/<int:category_id>/<int:page>', GoodsCategoryAPIView.as_view()),
    path("<str:sku_id>", GoodsDetailAPIView.as_view()),
]