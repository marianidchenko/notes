from django.contrib import admin

# Register your models here.
from notes.main.models import Profile, Note


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    pass
