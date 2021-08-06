

from rest_framework import serializers
from .models import WatchList,StreamPlatform,Review

class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'


class WatchListSerializer(serializers.ModelSerializer):
    watchlist = ReviewSerializer(many=True,read_only=True)

    class Meta:
        model = WatchList
        fields = '__all__'


class StreamPlatformSerializer(serializers.ModelSerializer):

    #this is comming from foreign key related name
    #watchlist = WatchListSerializer(many=True,read_only=True)
    #watchlist = serializers.StringRelatedField(many=True)
    #watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = '__all__'

