
from django.http import JsonResponse
from rest_framework.views import APIView
from  apps.user.models import User
from apps.user.serializers import UserSerializer
from utils.ResponseMessage import UserResponse
from utils.password_encode import get_md5


# Create your views here.
class UserAPIView(APIView):
    # def post(self, request):
    #     request.data['password'] = get_md5(request.data.get('password'))
    #
    #     # 反序列化呀，把json变成一个对象  [这是关键的一句话]
    #     user_data_serializer = UserSerializer(data=request.data)
    #     user_data_serializer.is_valid(raise_exception=True)
    #     user_data = user_data_serializer.save()
    #
    #     # 序列化一下，把json返回给前端对象
    #     user_ser = UserSerializer(instance=user_data)
    #     return JsonResponse(user_ser.data)
    def post(self, request):
        # request.data['password'] = get_md5(request.data.get('password'))

        # 反序列化呀，把json变成一个对象  [这是关键的一句话]
        user_data_serializer = UserSerializer(data=request.data)
        user_data_serializer.is_valid(raise_exception=True)
        # user_data = User.objects.create(**user_data_serializer.data)
        user_data = user_data_serializer.save()
        # 序列化一下，把json返回给前端对象
        user_ser = UserSerializer(instance=user_data)
        return UserResponse.success(data=user_ser.data)

        # return JsonResponse(user_ser.data)
    def get(self, request):
        email = request.GET.get('email')
        try:
            user_data = User.objects.get(email=email)
            user_ser = UserSerializer(user_data)
            return UserResponse.success(data=user_ser.data)
        except Exception as e:
            print(e)
            return UserResponse.failed("用户信息获取失败")