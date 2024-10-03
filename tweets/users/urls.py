from django.urls import path
from . import views
urlpatterns = [
    path('', views.see_all_users),
    path('<username>', views.see_user),
    path('<username>/tweets/', views.see_tweets_per_user),
]
