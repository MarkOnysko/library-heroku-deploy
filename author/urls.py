from django.urls import path
from . import views

app_name = 'author'

urlpatterns = [
    path('delete/<int:author_id>/', views.delete_author, name='delete'),
    path('detail/<int:author_id>/', views.author_detail, name='detail'),
    path('update/<int:author_id>/', views.update_author, name='update'),
    path('list/', views.authors_list, name='list'),
]
