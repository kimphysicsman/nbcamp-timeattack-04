from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from .models import User, UserType
from django.contrib.auth import login, authenticate, logout
from datetime import datetime

# 회원 기능
class UserAPI(APIView):
    permission_classes = [permissions.AllowAny]

    # 회원가입
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        email = request.data['email']
        type = request.data['type']

        if not username:
            raise ValueError('Users must have an username')

        type_obj = UserType.objects.get(id=type)
        user = User(
            email=email,
            username=username,
            type=type_obj
        )
        user.set_password(password)
        user.save()
        
        return Response({'message': '회원가입 완료!'})


# 로그인, 로그아웃 기능
class UserLoginAPI(APIView):
    permission_classes = [permissions.AllowAny]

    # 로그인 기능
    def post(self, request):
        user = authenticate(request, **request.data)
        
        if not user:
            msg = '아이디 또는 패스워드를 확인해주세요.'
            return Response({'message': msg})

        login(request, user)
        msg = '로그인 성공!'
        user.userlog.login_date = datetime.now()
        return Response({'message': msg,
                         'login_date': user.userlog.login_date,
                         'apply_date': user.userlog.apply_date,
                         }, status=status.HTTP_200_OK)

    # 로그아웃
    def delete(self, request):
        logout(request)
        msg = '로그아웃 성공!'
        return Response({'message': msg})