from django.contrib import admin

from todo.models import Task


# Register your models here.

class viewAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date', 'task_status')


admin.site.register(Task, viewAdmin)
