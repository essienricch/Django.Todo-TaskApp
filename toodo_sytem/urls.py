"""toodo_sytem URL Configuration

"""
from django.contrib import admin
from django.urls import path, include

import todo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include('todo.urls', namespace='todo')),
]
