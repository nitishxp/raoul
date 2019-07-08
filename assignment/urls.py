from django.urls import path

from order.views import (
    WorkOrderCreateView,
)

urlpatterns = [
    #     path('assign_order_to_worker',
    #          AssignOrdereToWorker.as_view(),
    #          name="w_assign_order"),
    #     path('fetch_orders',
    #          FetchWorkOrdersView.as_view(),
    #          name='fetch_work_orders'),
]
