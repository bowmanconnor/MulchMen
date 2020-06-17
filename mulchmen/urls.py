"""mulchmen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from appointments import views
from accounts import views as accounts_views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    path('orders/', views.orders, name='profile'),
    path('settings/account/', accounts_views.UserUpdateView.as_view(), name='edit_account'),
    path('contact/', views.contact, name='contact'),
    path('social-auth/', include('social_django.urls', namespace="social")),

    path('schedule/', views.schedule, name='schedule'),
    path('staff_schedule/', views.schedule_staff, name='schedule_staff'),
    path('appointments/', views.view_appointments, name='view_appointments'),
    path('appointments/<int:pk>/edit/', views.AppointmentUpdateView.as_view(), name='edit_appointment'),
    path('appointments/<int:pk>/view/', views.AppointmentDetailView.as_view(), name='view_appointment'),
    path('appointments/<int:pk>/confirm/', views.confirm_appointment, name='confirm_appointment'),
    path('appointments/<int:pk>/complete/', views.complete_appointment, name='complete_appointment'),
    path('appointments/<int:pk>/remove/', views.AppointmentDeleteView.as_view(), name='appointment_remove'),

    path('expenses/', views.view_expenses, name='view_expenses'),
    path('expenses/<int:pk>/edit/', views.ExpenseUpdateView.as_view(), name='edit_expense'),
    path('expenses/<int:pk>/view/', views.ExpenseDetailView.as_view(), name='view_expense'),
    path('expenses/new/', views.new_expense, name='new_expense'),
    path('expenses/<int:pk>/pay/', views.pay_expense, name='pay_expense'),
    path('expenses/<int:pk>/remove/', views.ExpenseDeleteView.as_view(), name='expense_remove'),





    path('signup/', accounts_views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name="login"),

    path('settings/account/', accounts_views.UserUpdateView.as_view(), name='my_account'),


    path('reset/',
        auth_views.PasswordResetView.as_view(
            template_name='password_reset.html',
            email_template_name='password_reset_email.html',
            subject_template_name='password_reset_subject.txt'
            ),
            name='password_reset'),
    path('reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm'),
    path('reset/complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'),

    path('settings/password/', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
        name='password_change'),
    path('settings/password/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
        name='password_change_done'),
]
