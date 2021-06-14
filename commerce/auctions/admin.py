from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *

# Register your models here.
admin.site.register(Comment)
admin.site.register(User)

class ListingAdmin(admin.ModelAdmin):
  exclude = ("category",)

admin.site.register(Listing, ListingAdmin)

admin.site.register(Category)