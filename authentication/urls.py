from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

app_name = 'authentication'

urlpatterns = [
    path('change_perms/<int:user_id>/', views.change_permissions, name='change_perms'),
    path('delete/<int:user_id>/', views.delete, name='delete'),
    path('deleted/', views.deleted, name='deleted'),
    path('denied/', views.denial, name='denied'),
    path('detail/<int:user_id>', views.detail, name='detail'),
    path('list/', views.list_all, name='users_list'),
    path('login/', auth_view.LoginView.as_view(template_name='auth/login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='auth/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('registered/', views.reg_done, name='reg_done'),
    path('update/<int:user_id>/', views.update, name='update'),
]
