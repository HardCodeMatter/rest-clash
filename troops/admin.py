from django.contrib import admin
from .models import Troops


@admin.register(Troops)
class TroopsAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'favorite_target', 'damage_type', 'targets',)
    list_filter = ('name', 'type', 'favorite_target', 'damage_type', 'targets',)

    fieldsets = [
        (None, {
            'fields': ('name', 'type', 'max_level',),
        }),
        ('Statistics', {
            'fields': (
            'favorite_target', 
            'damage_type', 
            'targets',
            'housing_space',
            'movement_speed',
            'training_time',
            'barracks_level_required',
            ),
        }),
    ]

    search_fields = ('name', 'type', 'favorite_target', 'damage_type', 'targets',)
    readonly_fields = ()
    ordering = ('-id',)
