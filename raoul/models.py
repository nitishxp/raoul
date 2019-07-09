from django.db import models


class Worker(models.Model):
    name = models.CharField(max_length=50, help_text='Name of Worker')
    company = models.CharField(max_length=50, help_text='Name of Company')
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'worker'

    def __str__(self):
        return self.name


class WorkOrder(models.Model):
    title = models.CharField(max_length=100, help_text='Title of Order')
    description = models.TextField(help_text='Description')
    deadline = models.DateField(help_text="Deadline of the order")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'orders'


class WorkerOrderAssignment(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'worker_order_assignment'
