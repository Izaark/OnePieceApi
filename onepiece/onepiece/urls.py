from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('api/character/', include('characters.api.urls', namespace='characters-api')),

]