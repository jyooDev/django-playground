from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from tweet.serializers import TweetSerializer
from rest_framework.exceptions import NotFound
from .models import User
from tweet.models import Tweet

class Users(APIView):
    # return Response(serializer.data)
    def get_users(self):
         return User.objects.all()
    
    def get(self, request):
            serializer = UserSerializer(self.get_users(), many=True)
            return Response(serializer.data)
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                 {
                    "message" : "New user is added.",
                    "new user": serializer.data,
                    "users": UserSerializer(self.get_users(),many=True).data        
                 }
            )
        else:
            return Response(serializer.errors)     


class SingleUser(APIView):
    def get_user(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            raise NotFound
    
    def get(self, request, username):
        user = self.get_user(username=username)
        responses = UserSerializer(user).data
        return Response(responses)
    
    def put(self, request, username):
        user = self.get_user(username)
        serializer = UserSerializer(
            user,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            updated_user = serializer.save()
            return Response(UserSerializer(updated_user).data)
        else:
            return Response(serializer.errors)
        
class UserTweets(APIView):
    def get_user(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            raise NotFound

    def get(self, request, username):
        user = self.get_user(username)
        user_tweets = Tweet.objects.select_related('user').filter(user=user)
        sorted_user_tweets = sorted(user_tweets, key=lambda t: t.likes_ct(), reverse=True)
        responses = TweetSerializer(sorted_user_tweets, many=True).data
        return Response(responses)
        
    def post(self, request, username):
        serializer = TweetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": f"New tweet is added by {username}.",
                    "new tweet": serializer.data
                }
            )