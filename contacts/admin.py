from django.contrib import admin
from contacts.models import Contact

class ContactAdmin(admin.ModelAdmin):
    model = Contact
    list_display = ('last_name', 'first_name')
    prepopulated_fields = {'slug': ('first_name', 'last_name')}


admin.site.register(Contact, ContactAdmin)