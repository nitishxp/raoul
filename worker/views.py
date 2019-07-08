import coreapi
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema
from rest_framework.generics import (
    ListCreateAPIView, )
from rest_framework import status
from rest_framework.views import APIView
from raoul.models import (
    Worker, )
from worker.serializers import (
    WorkerCreateSerializer, )


class WorkerCreateView(ListCreateAPIView):
    """
    get:
    Return list of workers

    post:
    Create a new worker
    """
    queryset = Worker.objects.all()
    serializer_class = WorkerCreateSerializer


class DeleteWorkerView(APIView):
    """
    delete:
    Delete a worker
    """
    schema = AutoSchema([
        coreapi.Field("worker_id",
                      required=True,
                      location='path',
                      description='Enter Worker Id')
    ])

    def delete(self, request, worker_id):
        Worker.objects.filter(pk=worker_id).delete()
        return Response({'detail': "Deleted Successfully"})
