from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TweetSerializer
from rest_framework.exceptions import NotFound
from .models import Tweet

# GET /api/v1/tweets: See all tweets
# POST /api/v1/tweets: Create a tweet
class Tweets(APIView):
    def get(self, request):
        tweets = Tweet.objects.all()
        sorted_tweets = sorted(tweets, key=lambda t: t.likes_ct(), reverse=True) #sort by likes count in descending order
        responses = TweetSerializer(sorted_tweets, many=True).data
        return Response(responses)
        
    def post(self, request):
        serializer = TweetSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": f"New tweet is added by.",
                    "new tweet": serializer.data
                }
            )

# GET /api/v1/tweets/<int:pk>: See a tweet
# PUT /api/v1/tweets/<int:pk>: Edit a tweet
# DELETE /api/v1/tweets/<int:pk>: Delete a tweet
class SingleTweet(APIView):
    def get_object(self, pk):
        try:
            return Tweet.objects.get(pk=pk)
        except Tweet.DoesNotExist:
            raise NotFound
        
    def get(self, request, pk):
        tweet = self.get_object(pk=pk)
        response = TweetSerializer(tweet).data
        return Response(response)
    
    def put(self, request, pk):
        tweet = Tweet.objects.get(pk=pk)
        serializer = TweetSerializer(
            tweet,
            data = request.data,
            partial = True,
        )
        if serializer.is_valid():
            updated_tweet = serializer.save()
            return Response(TweetSerializer(updated_tweet).data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        tweet = Tweet.objects.get(pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)