from django.contrib import admin
from .models import Tweet
from django.db.models import Q

# Register your models here.
@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    class ElonMuskFilter(admin.SimpleListFilter):
        title = "Filter by Elon Musk"

        parameter_name = "Elon Musk"
        def lookups(self, request, model_admin):
            return [
                ("contains", "contains Elon Musk"),
                ("not_contains", "not contains Elon Musk"),
            ]
        def queryset(self, request, tweet):
            ELON_MUSK = "Elon Musk"
            if(self.value() == "contains"):
                return tweet.filter(payload__icontains=ELON_MUSK)
            elif(self.value() == "not_contains"):
                return tweet.filter(~Q(payload__icontains=ELON_MUSK))

    list_display = ("user", "payload", "likes_ct", "created_at", "updated_at")
    list_filter =(
        "created_at",
        ElonMuskFilter,
    )
    search_fields=(
        "payload",
        "^user__username"
    )