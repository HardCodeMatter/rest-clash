from rest_framework import serializers

from .models import Troops, TroopsUpgradeStatistic


class TroopsUpgradeStatisticSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TroopsUpgradeStatistic
        fields = (
            'id',
            'level',
            'damage_per_second',
            'damage_per_attack',
            'hitpoints',
            'research_cost',
            'research_time',
            'laboratory_level_required',
        )


class TroopsSerializer(serializers.HyperlinkedModelSerializer):
    upgrade_statistic = TroopsUpgradeStatisticSerializer(many=True)

    class Meta:
        model = Troops
        fields = (
            'id',
            'name', 
            'type', 
            'max_level',
            'favorite_target',
            'damage_type',
            'targets',
            'housing_space',
            'movement_speed',
            'training_time',
            'barracks_level_required',

            'upgrade_statistic',
        )
