from django.contrib import admin

from . import models

class NotesAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_at', 'updated_at', 'likes')

admin.site.register(models.Notes, NotesAdmin)