from django.urls import include, path
from .views import *

urlpatterns = [
    path('', HomePage.as_view()),
    path('<int:pk>/', DetailFilmPage.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]