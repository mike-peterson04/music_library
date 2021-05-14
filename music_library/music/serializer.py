from rest_framework import serializers
from .models import Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'artist', 'album', 'release_date', 'likes']

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.artist = validated_data.get('artist', instance.artist)
        instance.album = validated_data.get('album', instance.album)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.likes = validated_data.get('likes', instance.likes)
        instance.save()
        return instance
