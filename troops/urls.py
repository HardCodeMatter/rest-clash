from django.urls import path

from .views import TroopsViewSet


troops_list = TroopsViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
troops_detail = TroopsViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = [
    path('troops/', troops_list, name='troops-list'),
    path('troops/<int:pk>/', troops_detail, name='troops-detail'),
]
