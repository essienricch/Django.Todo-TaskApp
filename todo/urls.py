import todo
from todo import views
from django.urls import path

app_name = 'todo'

urlpatterns = [

    path('home/', views.homepage, name='home'),
    path('create/', views.TaskCreateView.as_view(), name='create'),
    path('', views.TaskListView.as_view(), name='task_views'),
    path('<int:pk>/', views.TaskDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', views.TaskUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.TaskDeleteView.as_view(), name='delete'),
    path('contact/', views.contact_us, name='contactus')

]
