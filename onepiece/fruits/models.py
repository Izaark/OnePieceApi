from django.db import models
from django.urls import reverse_lazy
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.utils import timezone

class DevilFruit(models.Model):

	FRUIT_CHOICES = (
	(1, ("Paramecia")),
	(2, ("Logia")),
	(3, ("Zoan"))
	)

	name = models.CharField(null=False, blank=False, max_length=100)
	meaning = models.CharField(max_length=50)
	fruit_type = models.IntegerField(choices=FRUIT_CHOICES)
	abilities = models.TextField()
	debilities = models.TextField()
	apparence = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	class Meta:
		verbose_name = "DevilFruit"
		verbose_name_plural = "DevilFruits"
		ordering = ['-timestamp']

	def __str__(self):
		return self.name
