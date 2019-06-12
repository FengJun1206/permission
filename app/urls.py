from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.acc_login, name='login'),
    path('logout/', views.acc_logout, name='logout'),

    path('fina_state/', views.fina_state, name='fina_state'),
    path('staff_detail/', views.staff_detail, name='staff_detail'),
]
