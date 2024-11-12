from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import *
from .serializers import *
from rest_framework.generics import GenericAPIView, RetrieveAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status

class HomePage(APIView):
    
    def get(self, request):

        films = FilmModel.objects.all()

        return Response(FilmSerializer(films, many=True).data)
    

class DetailFilmPage(APIView):

    permission_classes = [IsAuthenticated,]

    def get(self, request, **kwargs):

        film_page = FilmModel.objects.get(pk=kwargs['pk'])
        return Response(FilmSerializer(film_page).data)
            

class UserRegistrationAPIView(APIView):
    permission_classes = (AllowAny, )
    # serializer_class = UserRegistrationsSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = RefreshToken.for_user(user)
        data = serializer.data
        data['tokens'] = {
            'refresh': str(token),
            'access': str(token.access_token)
        }

        return Response(data, status=status.HTTP_201_CREATED)
    

class UserLoginAPIView(APIView):
    permission_classes = (AllowAny,)
    
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        serializer = CustomUserSerializer(user)
        token = RefreshToken.for_user(user)
        data = serializer.data
        data['tokens'] = {
            'refresh': str(token),
            'access': str(token.access_token)
        }

        return Response(data, status=status.HTTP_200_OK)
    


class UserLogoutAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST) 
        

class UserInfo(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CustomUserSerializer
    def get_object(self):
        return self.request.user


class UserInfo(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        print(request.user)
        user = CustomUser.objects.get(email=request.user)
        
        return Response(CustomUserSerializer(user).data)
