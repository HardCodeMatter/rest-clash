from rest_framework import serializers
from django.core.exceptions import FieldDoesNotExist

from .models import Troops


class TroopsSerializer(serializers.HyperlinkedModelSerializer):
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
        )
    
    def to_representation(self, instance):
        data = super().to_representation(instance)

        for field in data:
            try:
                if instance._meta.get_field(field).choices:
                    data[field] = getattr(instance, f'get_{field}_display')()
            except FieldDoesNotExist:
                pass
        
        return data
