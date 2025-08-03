from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.views import UserCreateView  # Explicit import

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Authentication endpoints
    path('api/auth/', include([
        path('register/', UserCreateView.as_view(), name='register'),
        path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ])),
    
    path('api/products/', include('products.urls')),
]