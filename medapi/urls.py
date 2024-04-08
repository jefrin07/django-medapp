from django.urls import path
from . import views

urlpatterns = [
    path('signup',views.signup,name='signup_api'),
    path('login',views.login,name='login_api'),
    path('create',views.create_med,name='create_api'),
    path('list',views.list_med,name='list_api'),
    path('<int:pk>/update',views.update_med,name='update_api'),
    path('<int:pk>/delete',views.delete_med,name='delete_api'),
    path('search',views.search_med,name='search_api'),
]