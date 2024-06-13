
from django.urls import path

from chatt import views

app_name = "chatt"

urlpatterns = [
    path('home/', views.home , name ="home"),
    path('<str:room>/', views.room , name ="room"),
    path('checkview/', views.checkview , name ="checkview"),
    path('send', views.send , name ="send"),
    path('getMessages/<str:room>/', views.getMessages , name ="getMessages")
]