from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


# urlpatterns = [
#     path('', views.home, name=''),
#     path('create/', views.CatResultViewSet.as_view({'post': 'create'}), name='create'),
#     path('list/', views.CatResultViewSet.as_view({'get': 'list'}), name='list'),
#     path('<int:pk>/', views.CatResultViewSet.as_view({'get': 'retrieve'}), name='detail'),
#     path('<int:pk>/update/', views.CatResultViewSet.as_view({'put': 'update'}), name='update'),
#     path('<int:pk>/partial_update/', views.CatResultViewSet.as_view({'patch': 'partial_update'}), name='partial_update'),
#     path('<int:pk>/delete/', views.CatResultViewSet.as_view({'delete': 'destroy'}), name='delete'),
# ]

urlpatterns = [
    path('', views.home, name=''),
    path('create/', views.CreateAPIView.as_view(), name='create'),
    path('list/', views.ListAPIView.as_view(), name='list'),
    path('<int:pk>/', views.RetrieveAPIView.as_view(), name='detail'),
    path('<int:pk>/update/', views.UpdateAPIView.as_view(), name='update'),
    path('<int:pk>/delete/', views.DestroyAPIView.as_view(), name='delete'),

    path('token-generation/', obtain_auth_token),
    path('register/', views.UserRegister.as_view(), name='register'),
    

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]


"""
python manage.py drf_create_token niraj
Generated token 250435117e586dc547480ea371bc02dcccf220e8 for user niraj

python manage.py drf_create_token Staff-3
Generated token b26231312d57e0cb8068010188c498eff7222d1a for user Staff-3
"""
