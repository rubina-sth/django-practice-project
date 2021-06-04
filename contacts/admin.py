from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'listing', 'contact_date')
    search_fields = ('listing', 'name', 'contact_date')
    list_display_links = ('id', 'name')
    list_per_page = 25


admin.site.register(Contact, ContactAdmin)
