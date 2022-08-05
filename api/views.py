from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import RegisterSerializer
from .models import User
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class RegisterView(APIView):
    authentication_classes = ()
    permission_classes = ()
    allowed_methods = ['post']

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            password = serializer.validated_data.pop('password', None)
            user = User.objects.create(**serializer.validated_data)
            user.set_password(password)
            user.save()
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
