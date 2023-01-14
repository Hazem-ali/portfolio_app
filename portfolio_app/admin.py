from django.contrib import admin

from .models import ( About, ContactData, Service)
# Register your models here.


admin.site.register(About)
admin.site.register(ContactData)
admin.site.register(Service)
