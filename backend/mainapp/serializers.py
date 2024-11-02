
from rest_framework import serializers


class FilmSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    preview = serializers.ImageField()
    director = serializers.CharField()
