import coreapi
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema
from rest_framework import status
from rest_framework.views import APIView
from raoul.models import (WorkerOrderAssignment)
from assignment.serializers import (
    AssignOrderToWorkerSerializer,
    WorkOrderInfoSerializer,
)


class AssignOrdereToWorkerView(APIView):
    """
    post:
    Assign a order to worker
    """

    def get_serializer(self, *args, **kwargs):
        return AssignOrderToWorkerSerializer()

    def post(self, request):
        data = request.data
        serializer = AssignOrderToWorkerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=400)

        return Response({'detail': "Success"})


class FetchWorkOrdersView(APIView):
    """
    get:
    Fetch orders sorted by deadline can be specific to any worker or all
    """
    schema = AutoSchema(manual_fields=[
        coreapi.Field(
            "worker_id",
            location='query',
            description=
            'Enter worker id for fetching orders related to worker else ignore it'
        ),
    ])

    def get(self, request):

        worker_id = request.GET.get('worker_id')
        if worker_id:
            queryset = WorkerOrderAssignment.objects.filter(
                worker_id=worker_id)
        else:
            queryset = WorkerOrderAssignment.objects.all()

        queryset = queryset.order_by('order__deadline')

        serializer = WorkOrderInfoSerializer(queryset, many=True)
        return Response({'detail': serializer.data})
