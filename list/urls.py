from django.urls import path,re_path
from . import views

urlpatterns = [
    #path('', views.index),
    re_path(r'^$',views.index),
    re_path(r'add_todo/',views.add_todo),
    path('delete_todo/<int:todo_id>/', views.delete_todo),
]
