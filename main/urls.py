from django.urls import path,include
from main import views

urlpatterns = [
    path('',views.home,name='home'),
    path('create/',views.med_create,name='create'),
    path('update/<int:id>/', views.med_update, name='updatemed'),
    path('delete/<int:pk>/', views.med_delete, name='deletemed'),
    path('search/', views.med_search, name='searchmed'),
    path('logout/', views.user_logout, name='logout'), 
    ]