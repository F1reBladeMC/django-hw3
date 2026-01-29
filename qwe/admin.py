from django.contrib import admin
from .models import SiteSettings

# Register SiteSettings in admin
@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
	list_display = ('title', 'email', 'phone')
	search_fields = ('title', 'email')
