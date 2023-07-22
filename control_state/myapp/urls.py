from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.login,name='login'),
    path('regist',views.regist,name='regist'),
    path('regist_sql',views.regist_sql,name='regist_to_sql'),
    path('judgement',views.Login_judgement,name='Login_judgement'),
    path('flash',views.flash,name='flash'),
    path('muchao/<int:station_id>/<int:rightnum>',views.muchao,name='muchao'),
    path('station/<int:station_id>/<int:rightnum>',views.station,name='station'),
    path('mission_go/<int:station_id>/<int:rightnum>',views.mission_go,name='mission_go'),
    path('pictures/<int:station_id>',views.picture,name='picture'),
    path('add_station',views.add,name='add'),
    path('add_sql',views.add_to_sql,name='add_to_sql'),
    path('delete_station',views.delete,name='delete'),
    path('delete_sql',views.delete_to_sql,name='delete_to_sql'),
]