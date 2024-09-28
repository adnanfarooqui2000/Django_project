from django.urls import path
from app import views
urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('logout/',views.logout,name='logout'),
    path('register_Data/',views.register_Data,name='register_Data'),
]