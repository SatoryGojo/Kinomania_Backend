from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *


class HomePage(APIView):
    
    def get(self, request):

        films = FilmModel.objects.all()

        return Response(FilmSerializer(films, many=True).data)
    

class DetailFilmPage(APIView):

    permission_classes = [IsAuthenticated,]

    def get(self, request, **kwargs):

        film_page = FilmModel.objects.get(pk=kwargs['pk'])
        return Response(FilmSerializer(film_page).data)
            
