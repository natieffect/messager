from django.urls import path
from . import views

app_name="client"
urlpatterns = [
     path('',views.client_login,name='login'),
     path('logout/',views.client_logout,name="logout"),
     path('signup/',views.client_signup,name="signup"),
]