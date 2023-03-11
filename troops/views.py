from rest_framework import viewsets

from .serializers import TroopsSerializer, TroopsUpgradeStatisticSerializer
from .models import Troops, TroopsUpgradeStatistic


class TroopsViewSet(viewsets.ModelViewSet):
    queryset = Troops.objects.all().order_by('id')
    serializer_class = TroopsSerializer
