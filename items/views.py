from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
from items.serializers import UserSerializer, StoreSerializer
from rest_framework.authtoken.models import Token
from .models import Store


class RegisterUser(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response()
        else:
            return Response(serializer.errors)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            num = User.objects.get(username=username)
            token = Token.objects.get(user=num.id).key
            data = {'token': token}
            print(data)
            return Response(data)
        else:
            return Response("user dont exists", status=status.HTTP_404_NOT_FOUND)


class DataView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        for i in data:
            serializer = StoreSerializer(data=i)
            if serializer.is_valid():
                serializer.save()
        return Response(data)


class DataView2(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = Store.objects.all()
        serializer = StoreSerializer(data, many=True)
        return Response(serializer.data)
