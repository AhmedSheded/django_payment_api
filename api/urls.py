from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path, include
from .views import RegisterView


router = routers.DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
    path('login', obtain_jwt_token),
    path('register', RegisterView.as_view())
]