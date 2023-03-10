from rest_framework import viewsets

from .serializers import TroopsSerializer
from .models import Troops


class TroopsViewSet(viewsets.ModelViewSet):
    queryset = Troops.objects.all().order_by('id')
    serializer_class = TroopsSerializer
