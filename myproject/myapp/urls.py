from django.contrib import admin
from django.urls import path
from .views import signup_view, login_view, logout_view, dashboard_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
]