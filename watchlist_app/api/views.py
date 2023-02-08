from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView


class MovieListAV(APIView):

    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many= True)

        return Response(serializer.data)

    def post(self,request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MovieDetailAV(APIView):
    
    def get(self,request, pk):
        try:
            movie = Movie.objects.get(pk = pk)
        except Movie.DoesNotExist:
            return Response(data = {'Error': 'Movie Not Found'},status=status.HTTP_400_BAD_REQUEST)

        serializer = MovieSerializer(movie, many = False)
        return Response(serializer.data)

    def put(self,request, pk):
        movie = Movie.objects.get(pk = pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, pk):
        movie = Movie.objects.get(pk = pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# #Function Based Views
# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many= True)

#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_details(request, pk):
#     try:
#         movie = Movie.objects.get(pk = pk)

#         if request.method == 'GET':
#             serializer = MovieSerializer(movie, many = False)
#             return Response(serializer.data)

#         if request.method == 'PUT':
#             serializer = MovieSerializer(movie, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             else:
#                 return Response(status=status.HTTP_400_BAD_REQUEST)

#         if request.method == 'DELETE':
#             movie.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)

#     except Movie.DoesNotExist:
#         return Response(data = {'Error': 'Movie Not Found'},status=status.HTTP_400_BAD_REQUEST)

# # Process post not using serializing.
# @api_view(['GET','POST'])
# def movie_create(request):

#     if request.method == 'GET':
#         return Response('create endpoint')

#     if request.method == 'POST':
#         data = request.data
#         try:
#             name = data['name']
#             description = data['description']
#             active = data['active']

#             new_movie = Movie.objects.create()
#             new_movie.name = name
#             new_movie.description = description
#             new_movie.active = active
#             new_movie.save()
            
#             return Response(f'data {data}')
#         except:
#             return Response(f'Not enough data in  {data}')
        