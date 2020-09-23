from django.contrib import admin
from .models import Trouble
# Register your models here.

class TroubleAdmin(admin.ModelAdmin):
    search_fields = ['title']

admin.site.register(Trouble,TroubleAdmin)
