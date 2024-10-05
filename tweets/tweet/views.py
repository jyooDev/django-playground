from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TweetSerializer
from .models import Tweet

class Tweets(APIView):
    def get(self, request):
        tweets = Tweet.objects.all()
        sorted_tweets = sorted(tweets, key=lambda t: t.likes_ct(), reverse=True) #sort by likes count in descending order
        responses = TweetSerializer(sorted_tweets, many=True).data
        return Response(responses)
        