from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound, ParseError
from rest_framework import status
from django.contrib.auth import authenticate, login, logout

from tweet.serializers import TweetSerializer
from tweet.models import Tweet
from .serializers import UserSerializer, PrivateUserSerializer
from .models import User

from time import sleep

# GET /api/v1/users: See all users
# POST /api/v1/users: Create a user account with password
class Users(APIView):
    # return Response(serializer.data)
    def get_users(self):
         return User.objects.all()
    
    def get(self, request):
            serializer = UserSerializer(self.get_users(), many=True)
            return Response(serializer.data)
    
    def post(self, request):
        password = request.data.get("password")
        if not password:
            raise ParseError
        serializer = PrivateUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(password)
            user.save()
            serializer = PrivateUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)    


# GET /api/v1/users/<int:pk>: See user profile
class SingleUser(APIView):
    def get_user(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise NotFound
    
    def get(self, request, pk):
        user = self.get_user(pk=pk)
        responses = PrivateUserSerializer(user).data
        return Response(responses)
    
    def put(self, request, pk):
        user = self.get_user(pk)
        serializer = PrivateUserSerializer(
            user,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            updated_user = serializer.save()
            return Response(PrivateUserSerializer(updated_user).data)
        else:
            return Response(serializer.errors)
        
class UserTweets(APIView):
    def get_user(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        user = self.get_user(pk)
        user_tweets = Tweet.objects.select_related('user').filter(user=user)
        sorted_user_tweets = sorted(user_tweets, key=lambda t: t.likes_ct(), reverse=True)
        responses = TweetSerializer(sorted_user_tweets, many=True).data
        return Response(responses)
        
    def post(self, request, pk):
        serializer = TweetSerializer(data=request.data)
        user = self.get_user(pk)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": f"New tweet is added by {user.username}.",
                    "new tweet": serializer.data
                }
            )
        
# POST /api/v1/users/login: Log user in
class LogIn(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            raise ParseError
        user = authenticate(
            request,
            username=username,
            password=password,
        )
        if user:
            login(request, user)
            return Response({"ok": "Welcome!"})
        else:
            return Response(
                {"error": "wrong password"},
                status=status.HTTP_400_BAD_REQUEST,
            )


# POST /api/v1/users/logout: Log user out
class LogOut(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        sleep(5)
        logout(request)
        return Response({"ok": "bye!"})
    
# PUT /api/v1/users/password: Change password of logged in user.
class ChangePassword(APIView):

    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")
        if not old_password or not new_password:
            raise ParseError
        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            return Response(status=status.HTTP_200_OK)
        else:
            raise ParseError