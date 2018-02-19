from django.contrib import admin
from .models import Character, Affilation

# CharacterModelAdmin, upgrade the view Dajngoadmin for default
class CharacterModelAdmin(admin.ModelAdmin):

	list_display = ['name', 'epithet', 'timestamp']
	list_display_links = ['epithet']
	list_filter = ['timestamp']
	list_editable = ['name']
	search_fields = ['name', 'description']

admin.site.register(Character, CharacterModelAdmin)
admin.site.register(Affilation)
