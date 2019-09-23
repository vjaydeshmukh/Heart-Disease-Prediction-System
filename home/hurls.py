from django.urls import path
from . import views
from predict import views as p_views

urlpatterns = [
    path('', views.index, name='home'),
    path('hospital/', views.hospital, name='hospital'),
    path('hospital/<slug>/', views.hospital_detail, name='hospital_detail'),
    path('doctor/', views.doctor, name='doctor'),
    path('doctor/<slug>/', views.doctor_detail, name='doctor_detail'),
    path('blogs/', views.blog, name='blog'),
    path('blogs/<slug>/', views.blog_detail, name="detail"),
    path('search/', p_views.search, name='search'),
    path('login', p_views.login_view, name='login'),
    path('logout/', p_views.logout_view, name='logout'),
    path('signup/', p_views.register_view, name='signup'),
]