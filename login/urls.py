from django.contrib import admin
from django.urls import path
from login import views
urlpatterns = [
   path("",views.index,name='login'),
   path("todo",views.todo,name='todo'),
   path('add', views.addTodo, name='add'),
   path('complete/<todo_id>', views.completeTodo, name='complete'),
   path('deletecomplete', views.deleteCompleted, name='deletecomplete'),
   path('deleteall', views.deleteAll, name='deleteall'),
   path("reset",views.reset,name='reset'),
   path("home",views.home,name='home'),
   path("milestones",views.milestones,name='milestones'),
   path("workbench",views.workbench,name='workbench'),
   path("profile",views.profile,name='profile'),
   path("logout",views.logout,name='logout'),
   path("edit",views.edit,name='edit'),
   path("feedback",views.feedback,name='feedback'),
   path('calendar1/', views.CalendarView.as_view(), name='calendar'),
   path('event/new/', views.event, name='event_new'),
   path('event/edit/<int:event_id>/', views.event, name='event_edit'),
]