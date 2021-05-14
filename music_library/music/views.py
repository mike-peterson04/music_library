from django.shortcuts import render
from .models import Song
from .serializer import SongSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class SongList(APIView):

    def get(self, request):
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SongDetail(APIView):

    def get(self, request, song_id):
        try:
            song = Song.objects.get(pk=song_id)
            serializer = SongSerializer(song)
            return Response(serializer.data, status.HTTP_200_OK)

        except:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def put(self, request, song_id):
        try:
            song = Song.objects.get(pk=song_id)
        except:
            return Response(request.data, status=status.HTTP_400_BAD_REQUEST)
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            song = serializer.update(song, request.data)
            return Response(SongSerializer(song).data, status=status.HTTP_200_OK)

    def delete(self,request,song_id):
        try:
            song = Song.objects.get(pk=song_id)
        except:
            return Response(request.data, status=status.HTTP_400_BAD_REQUEST)
        deleted_song = SongSerializer(song)
        song.delete()
        return Response(deleted_song.data, status=status.HTTP_200_OK)

