from django.contrib import admin
from .models import Troops, TroopsUpgradeStatistic


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


@admin.register(TroopsUpgradeStatistic)
class TroopsUpgradeStatisticAdmin(admin.ModelAdmin):
    list_display = ('troops', 'level', 'laboratory_level_required',)
    list_filter = ('troops', 'level', 'hitpoints', 'research_cost', 'research_time', 'laboratory_level_required',)

    fieldsets = [
        (None, {
            'fields': ('troops', 'level', 'laboratory_level_required',),
        }),
        ('Statistics', {
            'fields': (
                'damage_per_second',
                'damage_per_attack', 
                'hitpoints', 
                'research_cost',
                'research_time',
            ),
        }),
    ]

    search_fields = ('troops', 'level', 'hitpoints', 'research_cost', 'research_time', 'laboratory_level_required',)
    readonly_fields = ()
    ordering = ('troops',)
