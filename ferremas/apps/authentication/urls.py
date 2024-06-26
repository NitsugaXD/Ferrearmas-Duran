from django.urls import path
from .views import CustomAuthToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path


urlpatterns = [
    path('login/', CustomAuthToken.as_view(), name='api_token_auth'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-token-auth/', CustomAuthToken.as_view(), name='custom_auth_token'),
]