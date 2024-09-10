from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, CustomTokenObtainView, UserPofileView

urlpatterns = [
    path("", RegisterView.as_view(), name="register"),
    path("login/", CustomTokenObtainView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("<str:username>/", UserPofileView.as_view(), name="user_pofile"),
]
