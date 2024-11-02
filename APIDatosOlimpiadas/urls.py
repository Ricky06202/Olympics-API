from django.urls import path, include, re_path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r"Olympics", views.OlympicsViewSet)

urlpatterns = [
    path("", include(router.urls)),
    re_path('login', views.login),
    re_path('register', views.register),
    re_path('profile', views.profile),
    re_path('olympics_data', views.olympics_data),
]