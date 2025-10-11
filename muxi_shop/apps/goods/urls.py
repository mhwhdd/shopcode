
from django.urls import path
from .views import GoodsCategoryAPIView,GoodsDetailAPIView
urlpatterns = [
    path('category/<int:category_id>/<int:page>', GoodsCategoryAPIView.as_view()),
    path("<str:sku_id>", GoodsDetailAPIView.as_view()),

]