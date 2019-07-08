from datetime import date
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import (
    ModelSerializer,
    IntegerField,
    CharField,
    DateField,
    Serializer,
)

from raoul.models import (
    Worker,
    WorkOrder,
    WorkerOrderAssignment,
)


class WorkerCreateSerializer(ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'


class WorkOrderCreateSerializer(ModelSerializer):
    class Meta:
        model = WorkOrder
        fields = '__all__'


class AssignOrderToWorkerSerializer(Serializer):

    worker_id = IntegerField(label='Worker Id')
    order_id = IntegerField(label='Order Id')

    def validate(self, data):
        worker_id = data.get('worker_id')
        order_id = data.get('order_id')

        # check for valid workers
        try:
            worker_obj = Worker.objects.get(pk=worker_id)
        except Worker.DoesNotExist as e:
            raise ValidationError("Invalid Worker Id")

        # check whether assignment is not for expired order
        try:
            order_obj = WorkOrder.objects.get(pk=order_id)
        except WorkOrder.DoesNotExist as e:
            raise ValidationError("Invalid Order Id")

        if order_obj.deadline < date.today():
            raise ValidationError("Cannot assign worker to expired order")

        # check for order count
        if WorkerOrderAssignment.objects.filter(
                order_id=order_id).count() >= 5:
            raise ValidationError("Order has reached maximum worker limit")

        return data

    def create(self, data):

        WorkerOrderAssignment.objects.create(worker_id=data.get('worker_id'),
                                             order_id=data.get('order_id'))
        return {}


class WorkOrderInfoSerializer(ModelSerializer):
    order = WorkOrderCreateSerializer()
    worker = WorkerCreateSerializer()
    assignment_id = IntegerField(source='id')

    class Meta:
        model = WorkerOrderAssignment
        fields = ['assignment_id', 'order', 'worker', 'created_at']
