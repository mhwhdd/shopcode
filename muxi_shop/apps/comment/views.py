from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin,ListModelMixin

from apps.comment.models import Comment
from apps.comment.serializers import CommentSerializer
from utils.ResponseMessage import CommentResponse


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

class CommentAPIView(APIView):
    def get(self,request):
        sku_id = request.GET.get('sku_id')
        page = request.GET.get('page')
        start = (int(page)  - 1) * 15
        end = int(page)* 15
        db_result = Comment.objects.filter(sku_id=sku_id).all()[start:end]
        print("========{}".format(db_result) )
        ser_data = CommentSerializer(instance=db_result, many=True)
        print(ser_data.data)
        return  CommentResponse.success(ser_data.data)

        # return JsonResponse("oh")
        # return CommentResponse("ok") #CommentResponse(ser_data.data)

class CommentCountAPIView(APIView):
    def get(self,request):
        sku_id = request.GET.get('sku_id')
        db_result = Comment.objects.filter(sku_id=sku_id).count()
        # ser_data = CommentSerializer(instance=db_result,many=True)
        return CommentResponse.success(db_result)