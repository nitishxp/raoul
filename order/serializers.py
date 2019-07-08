from datetime import date
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import (
    ModelSerializer, )
from raoul.models import (
    WorkOrder, )


class WorkOrderCreateSerializer(ModelSerializer):
    class Meta:
        model = WorkOrder
        fields = '__all__'
