from rest_framework.serializers import ModelSerializer

from characters.models import Character

class CharacterListSerializer(ModelSerializer):

	class Meta:
		model = Character
		fields = ['name', 'description', 'apparence', 'epithet', 'bounty', 'activities']