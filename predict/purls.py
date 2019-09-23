from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('predict_disease/', views.index, name='predict'),
    path('myhistory/', views.history, name='history'),
    path('attribute/', views.attribute, name='attribute'),
    path('attribute/<slug>/', views.attribute_detail, name='attr_detail'),
    path('activate/(P<uidb64>[0-9A-Za-z_\\-]+)/(P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
         views.activate, name='activate'),

    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='prediction/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='prediction/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='prediction/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='prediction/password_reset_complete.html'), name='password_reset_complete'),

]