from django.db import models


class Troops(models.Model):
    name = models.CharField(('name'), max_length=50)
    max_level = models.IntegerField(('max level'))
    type = models.CharField(('type'), max_length=50, choices=[
        ('elixir', 'Elixir Troops'),
        ('dark_elixir', 'Dark Elixir Troops')
    ])

    favorite_target = models.CharField(('favorite target'), max_length=50, choices=[
        ('any', 'Any'),
        ('defenses', 'Defenses'),
        ('air_defense', 'Air Defense'),
        ('resources', 'Resources (Damage x2)'),
        ('walls', 'Walls (Damage x40)'),
        ('heroes', 'Heroes (Damage x4)'),
    ])
    damage_type = models.CharField(('damage type'), max_length=50, choices=[
        ('single', 'Single Target'),
        ('area', 'Area Splash'),
    ])
    targets = models.CharField(('targets'), max_length=50, choices=[
        ('ground', 'Ground'),
        ('ground_air', 'Ground & Air'),
    ])
    housing_space = models.IntegerField(('housing space'))
    movement_speed = models.IntegerField(('movement speed'))
    training_time = models.IntegerField(('training time'))
    barracks_level_required = models.IntegerField(('barracks level required'))

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Troop'
        verbose_name_plural = 'Troops'


class TroopsUpgradeStatistic(models.Model):
    troops = models.ForeignKey(Troops, on_delete=models.CASCADE, related_name='upgrade_statistic')
    
    level = models.IntegerField(('level'))
    damage_per_second = models.IntegerField(('damage per second'))
    damage_per_attack = models.IntegerField(('damage per attack'))
    hitpoints = models.IntegerField(('hitpoints'))
    research_cost = models.IntegerField(('research cost'))
    research_time = models.IntegerField(('research time'))
    laboratory_level_required = models.IntegerField(('laboratory level required'))

    def __str__(self):
        return f'{self.troops}'
    
    class Meta:
        verbose_name = 'Upgrade statistic'
        verbose_name_plural = 'Upgrade statistics'
