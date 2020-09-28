from django.contrib import admin
from .models import Trouble, Tr_Comment
# Register your models here.

class TroubleAdmin(admin.ModelAdmin):
    search_fields = ['title']

admin.site.register(Trouble,TroubleAdmin)
admin.site.register(Tr_Comment)
