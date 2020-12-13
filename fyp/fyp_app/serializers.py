from rest_framework import serializers
from fyp_app.models import Tweet

# Tweet Serializer


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = '__all__'
