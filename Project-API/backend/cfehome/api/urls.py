from django.urls import path, include

from . import views
#from .views import api_home

from rest_framework.authtoken.views import obtain_auth_token

# api/
urlpatterns = [
    path('', views.api_home), # localhost:8000/api/
    #path('products/', include('products.urls')),
    path('auth/', obtain_auth_token)
]