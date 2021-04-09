from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [
    path('list/', views.list_all, name='list_all'),
    path('detail/<int:book_id>/', views.book_detail, name='detail'),
    path('update/<int:book_id>/', views.update, name='update'),
    path('delete/<int:book_id>/', views.delete, name='delete'),
    path('', views.create, name='create'),
]