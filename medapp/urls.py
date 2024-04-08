from django.contrib import admin
from django.urls import path,include
from registration import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login_page,name='login'),
    path('signup/',views.signup_page,name='signup'),
    path('home/',include('main.urls')),
    path('medapi/', include('medapi.urls')),
]
