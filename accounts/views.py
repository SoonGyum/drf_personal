from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from .serializers import (
    UserSerializer,
    CustomTokenObtainPairSerializer,
    UserPofileSerializer,
)
from rest_framework_simplejwt.views import TokenObtainPairView


class RegisterView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "회원가입 완료"},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomTokenObtainView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(
            {"detail": "아이디나 비밀번호가 잘못되었습니다."},
            status=status.HTTP_401_UNAUTHORIZED,
        )


class UserPofileView(RetrieveAPIView):
    serializer_class = UserPofileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
