import coreapi

from django.http import Http404
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    ListCreateAPIView,
    GenericAPIView,
)
from rest_framework import status
from rest_framework.views import APIView
from django.db.models import Count
from raoul.models import (
    WorkOrder, )
from order.serializers import (
    WorkOrderCreateSerializer, )


class WorkOrderCreateView(ListCreateAPIView):
    """
    get:
    Return list of all orders within deadline

    post:
    Create a new work order
    """
    queryset = WorkOrder.objects.all()
    serializer_class = WorkOrderCreateSerializer