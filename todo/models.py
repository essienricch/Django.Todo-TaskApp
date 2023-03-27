from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


# Create your models here.

class Task(models.Model):
    status_option = [('in progress', 'IN PROGRESS'),
                     ('completed', 'COMPLETED')]

    title = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    task_status = models.CharField(max_length=20, choices=status_option, default='in progress')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task_views')
