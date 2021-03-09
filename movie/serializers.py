from rest_framework import serializers
from .models import *


class ActorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__',


class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = 'genre_name',


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__',


class MovieSerializer(serializers.ModelSerializer):
    starring = ActorSerializers(many=True)
    director = ActorSerializers(many=True)
    genre = GenreSerializers(many=True)
    category = CategorySerializers(many=False)

    class Meta:
        model = Movie
        fields = '__all__',


class MovieShotsSerializers(serializers.ModelSerializer):
    movie = MovieSerializer()

    class Meta:
        model = Category
        fields = '__all__',


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        exclude = "movie",


class RatingSerializers(serializers.ModelSerializer):
    movie = MovieSerializer()

    class Meta:
        model = Category
        fields = '__all__',


class MovieMainSerializer(serializers.ModelSerializer):
    genre = GenreSerializers(many=True)

    class Meta:
        model = Movie
        fields = ["title", "poster", "published_date", "genre"]
