from django.urls import path

from api.views import (
    WorkerCreateView,
    WorkOrderCreateView,
    AssignOrdereToWorker,
    DeleteWorkerView,
    FetchWorkOrdersView,
)
urlpatterns = [
    path('worker', WorkerCreateView.as_view(), name="worker"),
    path('delete_worker/<int:worker_id>',
         DeleteWorkerView.as_view(),
         name="delete worker"),
    path('order', WorkOrderCreateView.as_view(), name="order"),
    path('assign_order_to_worker',
         AssignOrdereToWorker.as_view(),
         name="w_assign_order"),
    path('fetch_orders',
         FetchWorkOrdersView.as_view(),
         name='fetch_work_orders'),
]
