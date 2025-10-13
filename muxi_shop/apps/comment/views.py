from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ViewSetMixin
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin,ListModelMixin

from apps.comment.models import Comment
from apps.comment.serializers import CommentSerializer


# Create your views here.
class CommentGenericAPIView( ViewSetMixin,
                             GenericAPIView,
                             CreateModelMixin,
                             RetrieveModelMixin,
                             UpdateModelMixin,
                             DestroyModelMixin,
                             ListModelMixin):
    # ViewSetMixin,
    # GenericAPIView,
    # CreateModelMixin,
    # RetrieveModelMixin,
    # UpdateModelMixin,
    # DestroyModelMixin,
    # ListModelMixin
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # ViewSetMixin 结合router使用 在as_view中可配置自定义方法
    def single(self,request,pk):
        print("我是查询一个=====")
        return self.retrieve(request,pk)
    def my_list(self,request):
        print("我是查询多个=====")
        return self.list(request)
    def edit(self,request,pk):
        print("我是更新=====")
        return self.update(request,pk)
    def my_save(self,request,pk):
        print("我是保存=====")
        return self.create(request,pk)
    def my_delete(self,request,pk):
        print("我是删除=====")
        return self.destroy(request,pk)

