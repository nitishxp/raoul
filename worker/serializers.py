from rest_framework.serializers import (
    ModelSerializer, )
from raoul.models import (
    Worker, )


class WorkerCreateSerializer(ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'
