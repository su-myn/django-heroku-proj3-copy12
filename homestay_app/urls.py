from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('table_todo_list/', views.todoList, name='todoList'),
    path('table_contact_list/', views.contactList, name='contactList'),
    path('table_complain_list/', views.complainList, name='complainList'),
    path('table_repair_list/', views.repairList, name='repairList'),
    path('table_replace_list/', views.replaceList, name='replaceList'),
    path('table_task_list/', views.taskList, name='taskList'),
    path('form_todo_list/', views.formTodoList, name='formTodoList'),
    path('form_contact_list/', views.formContactList, name='formContactList'),
    path('form_complain_list/', views.formComplainList, name='formComplainList'),
    path('form_repair_list/', views.formRepairList, name='formRepairList'),
    path('form_replace_list/', views.formReplaceList, name='formReplaceList'),
    path('form_task_list/', views.formTaskList, name='formTaskList'),
    path('update_task_list/<str:pk>', views.updateTaskList, name='updateTaskList'),
    path('delete_task_list/<str:pk>', views.deleteTaskList, name='deleteTaskList'),
    path('update_todo_list/<str:pk>', views.updateTodoList, name='updateTodoList'),
    path('delete_todo_list/<str:pk>', views.deleteTodoList, name='deleteTodoList'),
    path('update_contact_list/<str:pk>', views.updateContactList, name='updateContactList'),
    path('delete_contact_list/<str:pk>', views.deleteContactList, name='deleteContactList'),
    path('update_complain_list/<str:pk>', views.updateComplainList, name='updateComplainList'),
    path('delete_complain_list/<str:pk>', views.deleteComplainList, name='deleteComplainList'),
    path('update_repair_list/<str:pk>', views.updateRepairList, name='updateRepairList'),
    path('delete_repair_list/<str:pk>', views.deleteRepairList, name='deleteRepairList'),
    path('update_replace_list/<str:pk>', views.updateReplaceList, name='updateReplaceList'),
    path('delete_replace_list/<str:pk>', views.deleteReplaceList, name='deleteReplaceList'),

]