from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
# from rest_framework.pagination import LimitOffsetPagination
from .serializers import *
from .models import *


class MovieDetailView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie, many=True, context={"request": request})
        rev = Reviews.objects.all()
        rev_ser = ReviewSerializers(rev, many=True)
        return Response({'movie': serializer.data, 'reviews': rev_ser.data})


class MovieMainView(APIView):
    def get(self, request):
        movie = Movie.objects.all()
        serializer = MovieMainSerializer(movie, many=True, context={"request": request})
        return Response({'movie': serializer.data})
