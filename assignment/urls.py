from django.urls import path

from assignment.views import (
    AssignOrdereToWorkerView,
    FetchWorkOrdersView,
)

urlpatterns = [
    path('assign_order_to_worker',
         AssignOrdereToWorkerView.as_view(),
         name="w_assign_order"),
    path('fetch_orders',
         FetchWorkOrdersView.as_view(),
         name='fetch_work_orders'),
]
