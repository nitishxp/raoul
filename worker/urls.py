from django.urls import path

from worker.views import (
    WorkerCreateView,
    DeleteWorkerView,
)
urlpatterns = [
    path('', WorkerCreateView.as_view(), name="worker"),
    path('delete_worker/<int:worker_id>',
         DeleteWorkerView.as_view(),
         name="delete worker"),
]
