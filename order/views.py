from django.shortcuts import render, get_object_or_404, redirect
from .models import Order
from .forms import CreateOrderForm, UpdateOrderForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone


@login_required(login_url='authentication:login')
def view_all_orders(request):
    if request.user.role != 1:
        return redirect('authentication:denied')
    order_list = Order.objects.all()
    return render(request, 'order/orders_list.html', {'order_list': order_list})


@login_required(login_url='authentication:login')
def detail_order(request, order_id):
    if request.user.role != 1:
        return redirect('authentication:denied')
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order/detail.html', {'order': order})


@login_required(login_url='authentication:login')
def create_order(request):
    if request.user.role != 1:
        return redirect('authentication:denied')
    if request.method == 'POST':
        form = CreateOrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.book.count -= 1
            order.book.save()
            order.save()
            return redirect('order:view_all_orders')
    else:
        form = CreateOrderForm()
    return render(request, 'order/create.html', {'form': form})


@login_required(login_url='authentication:login')
def update_order(request, order_id):
    if request.user.role != 1:
        return redirect('authentication:denied')
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        form = UpdateOrderForm(instance=order, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('order:view_all_orders')
    else:
        form = UpdateOrderForm(instance=order)
    return render(request, 'order/update.html', {'form': form})


@login_required(login_url='authentication:login')
def delete_order(request, order_id):
    if request.user.role != 1:
        return redirect('authentication:denied')
    order = get_object_or_404(Order, id=order_id)
    order.book.count += 1
    order.book.save()
    order.delete()
    return redirect('order:view_all_orders')


@login_required(login_url='authentication:login')
def borrow_book(request, book_id):
    order = Order(book_id=book_id, user_id=request.user.id)
    order.book.count -= 1
    order.book.save()
    order.save()
    return redirect('authentication:detail', user_id=request.user.id)


@login_required(login_url='authentication:login')
def close_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.user.role != 1 and request.user.id != order.user.id:
        return redirect('authentication:denied')
    order.end_at = timezone.now()
    order.book.count += 1
    order.book.save()
    order.save()
    return redirect('authentication:detail', user_id=order.user.id)