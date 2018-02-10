from django.db import models
from django.urls import reverse_lazy
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.utils import timezone
from django.contrib.postgres.fields import JSONField
from fruits.models import DevilFruit

# Character: class is the table in DB ! 
class Character(models.Model):

	name = models.CharField(null=False, blank=False, max_length=100)
	slug = models.SlugField(unique=True)
	description = models.TextField()
	apparence = models.TextField()
	epithet = models.CharField(max_length=200, unique=True)
	bounty = models.IntegerField(default=0)
	activities = models.CharField(max_length=250)
	abilities = JSONField() #allow add object list:
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	#relations
	fruit = models.OneToOneField(DevilFruit, on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Character"
		verbose_name_plural = "Characters"
		ordering = ['-timestamp']#order the characters since most new to oldest

	def __str__(self):
		return self.name


#Character.objects.create(name='Monkey D Luffy', slug='Momkey-D-luffy', description='Es el protagonista principal de la serie de manga y anime One Piece. Comió una fruta del diablo de clase paramecia llamada fruta Gomu Gomu', apparence='Luffy lleva una chaqueta roja de manga larga con 4 botones (Con el pecho descubierto), con una banda amarilla atada a la cintura', epithet='Sombrero de Paja (麦わら Mugiwara)', bounty=500000000, activities='ser rey de los piratas', abilities= {"abilidades": ["haky del rey", "Haky de Obersvacion", Haky de Armadura"]})
#INSERT INTO fruits_devilfruit Values(1, 'Gomu Gomu', 'nose', 1, 'estirarse', 'agua', 'morada', '2017-02-10 12:01:20');