from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from tweet.serializers import TweetSerializer
from rest_framework.exceptions import NotFound
from .models import User

@api_view(["GET", "POST"])
def see_all_users(request):
    users = User.objects.all()
    # return Response(serializer.data)
    if request.method == "GET":
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)
    elif request.method == "POST":
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            return Response(
                 {
                    "message" : "New user is added.",
                    "users": UserSerializer(users,many=True).data        
                 }
            )
        else:
            return Response(serializer.errors)     


@api_view(["GET", "POST"])
def see_user(request, username):
    try:
        user = User.objects.get(pk=username)
    except User.DoesNotExist:
        raise NotFound
    if request.method == "GET":
            serializer = UserSerializer(user)
            return Response(serializer.data)
    elif request.method == "POST":
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
        
@api_view()
def see_tweets_per_user(request, username):
    try:
        user = User.objects.get(pk=username)
        user_tweets = user.tweets.all()
        print(user_tweets)
        serializer = TweetSerializer(user_tweets, many=True)
        return Response(serializer.data)
    except User.DoesNotExist:
        raise NotFound