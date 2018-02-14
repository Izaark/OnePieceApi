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
# Affilations: class is the table in DB ! 
class Affilation(models.Model):

	name = models.CharField(blank=False,  null= False, max_length=80)
	total_bounty = models.IntegerField(default=0) #TODO: create funtion depends Character bounty
	count_members = models.IntegerField(default=0)#TODO: create funtion depends members count
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	#relations
	member = models.ManyToManyField(Character)

	class Meta:
		verbose_name = "Affilation"
		verbose_name_plural = "Affilation"
		ordering = ['-timestamp']

	def __str__(self):
		return self.name





#create_slug: use for create slug whit the title name
def create_slug(instance, new_slug=None):
	slug = slugify(instance.name)
	if new_slug is not None:
		slug = new_slug
	qs = Character.objects.filter(slug=slug).order_by('-id')#queryset for filter by slug, ordering from highest to lowest
	exists = qs.exists()
	if exists:
		new_slug = '%s-%s' %(slug, qs.first().id)
		return create_slug(instance, new_slug=new_slug)	#reuturn recursive function with the new slug
	return slug


#pre_save_Character_receiver: if haven't slug the instance.slug (instance.slug = Character.slug), create_slug do it
def pre_save_Character_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)

pre_save.connect(pre_save_Character_receiver, sender=Character)


''' Character.objects.create(name='Monkey D Luffy', slug='Momkey-D-luffy', description='Es el protagonista principal de la serie de manga y anime One Piece. Comió una fruta del diablo de clase paramecia llamada fruta Gomu Gomu', apparence='Luffy lleva una chaqueta roja de manga larga con 4 botones (Con el pecho descubierto), con una banda amarilla atada a la cintura', epithet='Sombrero de Paja (麦わら Mugiwara)', bounty=500000000, activities='ser rey de los piratas', abilities= {"abilidades": ["haky del rey", "Haky de Obersvacion", "Haky de Armadura"]})
INSERT INTO fruits_devilfruit Values(1, 'Gomu Gomu', 'nose', 1, 'estirarse', 'agua', 'morada', '2017-02-10 12:01:20'); '''