from django.contrib import admin
from .models import UserReview, Restaurant

admin.site.register(Restaurant)
admin.site.register(UserReview)