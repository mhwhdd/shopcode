from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, \
    ListModelMixin

from apps.address.models import UserAddress
from apps.address.serializers import AddressSerializer


# Create your views here.
class AddressGenericAPIView(GenericAPIView,
                            CreateModelMixin,
                            RetrieveModelMixin,
                            UpdateModelMixin,
                            DestroyModelMixin):
    # 继承 CreateModelMixin 封装实现创建保存功能
    queryset = UserAddress.objects.all()
    serializer_class = AddressSerializer
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def get(self, request, pk):
        # 继承 RetrieveModelMixin 封装实现单个查询功能 pk 主键
        return self.retrieve(request,pk)
    def put(self, request,pk):
        # 继承 UpdateModelMixin 封装实现修改功能
        return self.update(request,pk)
    def delete(self, request,pk):
        # 继承 DestroyModelMixin 封装实现删除功能
        return self.destroy(request,pk)

class AddressListGenericAPIView(GenericAPIView,
                                 ListModelMixin,):
    queryset = UserAddress.objects.all()
    serializer_class = AddressSerializer
    def get(self,request):
        # 继承 ListModelMixin 封装实现请求多个
        return  self.list(request)