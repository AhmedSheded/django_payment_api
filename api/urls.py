from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path


router = routers.DefaultRouter()

urlpatterns = [
    path('login/', obtain_jwt_token)
]