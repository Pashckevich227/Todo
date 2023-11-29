from django.contrib import admin
from django.urls import path
from todoproject.views import todoView, addTodoItem, deleteTodoView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', todoView),
    path('addTodoItem/', addTodoItem),
    path('deleteTodoItem/<int:i>/', deleteTodoView),
]
