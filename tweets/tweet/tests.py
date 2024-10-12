from rest_framework.test import APITestCase
from rest_framework import status
from .models import Tweet
from users.models import User

class TestTweets(APITestCase):
    TWEETS_URL = "/api/v1/tweets/"
    TESTUSER = "Tweet Test User"
    PAYLOAD = "Tweet Test Payload"
    
    def setUp(self):
        # Create a user and tweet for testing
        self.user = User.objects.create(username=self.TESTUSER)
        self.tweet = Tweet.objects.create(
            user=self.user,
            payload=self.PAYLOAD
        )
        self.tweet_url_with_id = f"{self.TWEETS_URL}{self.tweet.pk}/"

    # Test GET /api/v1/tweets/ to retrieve all tweets
    def test_get_tweets(self):
        response = self.client.get(self.TWEETS_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["user"], self.user.pk)
        self.assertEqual(data[0]["payload"], self.PAYLOAD)

    # Test POST /api/v1/tweets/ to create a new tweet
    def test_create_tweet(self):
        new_tweet_data = {
            "user": self.user.id,
            "payload": "New Tweet"
        }
        response = self.client.post(self.TWEETS_URL, data=new_tweet_data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["new tweet"]["payload"], "New Tweet")

    # Test GET /api/v1/tweets/<int:pk> to retrieve a specific tweet
    def test_get_single_tweet(self):
        response = self.client.get(self.tweet_url_with_id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()

        self.assertEqual(data["user"], self.user.pk)
        self.assertEqual(data["payload"], self.PAYLOAD)

    # Test PUT /api/v1/tweets/<int:pk> to update a specific tweet
    def test_update_tweet(self):
        updated_tweet_data = {
            "payload": "Updated Tweet Payload"
        }
        response = self.client.put(self.tweet_url_with_id, data=updated_tweet_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["payload"], "Updated Tweet Payload")

    # Test DELETE /api/v1/tweets/<int:pk> to delete a specific tweet
    def test_delete_tweet(self):
        response = self.client.delete(self.tweet_url_with_id)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Tweet.objects.filter(pk=self.tweet.pk).exists())
