from django.contrib import admin
from django.urls import path, include

from apps import goods
from  apps import cart
from apps.menu.views import GoodsMainMenu,GoodsSubMenu
from muxi_shop import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main_menu/', GoodsMainMenu.as_view()),
    path('sub_menu/', GoodsSubMenu.as_view()),
    path("goods/",include("goods.urls")),
    path("cart/", include("cart.urls")),
    path("user/", include("user.urls")),
    path("order/", include("order.urls")),
    path("address/", include("address.urls")),
    path("comment/", include("comment.urls")),

]
if settings.DEBUG:
    pass
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)