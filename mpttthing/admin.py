from django.contrib import admin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
from mpttthing.models import File

class FileAdmin(DraggableMPTTAdmin):
    mptt_indent_field = 'name'