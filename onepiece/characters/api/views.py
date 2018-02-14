from rest_framework.generics import ListAPIView
from .serializers import CharacterListSerializer
from characters.models import Character

class CharacterListAPIView(ListAPIView):
	queryset = Character.objects.all()
	serializer_class = CharacterListSerializer
