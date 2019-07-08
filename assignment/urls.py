from django.urls import path

from assignment.views import (
    AssignOrdereToWorkerView,
    FetchWorkOrdersView,
)

urlpatterns = [
    path('', FetchWorkOrdersView.as_view(), name='fetch_work_orders'),
    path('create', AssignOrdereToWorkerView.as_view(), name="w_assign_order"),
]
