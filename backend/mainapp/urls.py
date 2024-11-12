from django.urls import include, path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('', HomePage.as_view()),
    path('<int:pk>/', DetailFilmPage.as_view()),


    path('api/register/', UserRegistrationAPIView.as_view()),
    path('api/login/', UserLoginAPIView.as_view()),
    path('api/logout/', UserLogoutAPIView.as_view()),
    path('api/refresh/', TokenRefreshView.as_view()),
    path('api/user/', UserInfo.as_view()),
]