from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('', views.create_order, name='create_order'),
    path('borrow_book/<int:book_id>/', views.borrow_book, name='borrow_book'),
    path('close_order/<int:order_id>/', views.close_order, name='close_order'),
    path('list/', views.view_all_orders, name='view_all_orders'),
    path('update/<int:order_id>/', views.update_order, name='update_order'),
    path('delete/<int:order_id>/', views.delete_order, name='delete_order'),
    path('detail/<int:order_id>/', views.detail_order, name='detail_order'),
]