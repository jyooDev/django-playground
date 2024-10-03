from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TweetSerializer
from .models import Tweet

@api_view(["GET"])
def see_all_tweets(request):
    tweets = Tweet.objects.all()
    serializer = TweetSerializer(tweets, many=True)
    return Response(serializer.data)
        