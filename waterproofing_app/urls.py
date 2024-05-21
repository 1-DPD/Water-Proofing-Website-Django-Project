from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('services/', views.services, name='services'),
    path('submit_inquiry/<int:service_id>/', views.submit_inquiry, name='submit_inquiry'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('customer/dashboard/', views.customer_dashboard, name='customer_dashboard'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
   


]
