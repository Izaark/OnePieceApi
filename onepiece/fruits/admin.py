from django.contrib import admin
from .models import DevilFruit

# DevilFruitModelAdmin, upgrade the view Dajngoadmin for default
class DevilFruitModelAdmin(admin.ModelAdmin):

	list_display = ['name', 'meaning', 'fruit_type', 'timestamp']
	list_display_links = ['fruit_type']
	list_filter = ['timestamp']
	list_editable = ['name']
	search_fields = ['name', 'meaning', 'fruit_type']

admin.site.register(DevilFruit, DevilFruitModelAdmin)
