from django.contrib import admin

from pdf.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
