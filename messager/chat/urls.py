from django.urls import path
from . import views

app_name="chat"
urlpatterns=[
    path('home/',views.chat_homepage,name='homepage'),
    path('delete/',views.chat_deletemessage,name='delete'),
    path('update/',views.chat_updatemessage,name='update')
]