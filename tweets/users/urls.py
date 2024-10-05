from django.urls import path
from . import views
urlpatterns = [
    path('', views.Users.as_view()),
    path('<username>/', views.SingleUser.as_view()),
    path('<username>/tweets/', views.UserTweets.as_view()),
]
