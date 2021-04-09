from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookCreateForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='authentication:login')
def list_all(request):
    books_list = Book.objects.all()
    return render(request, 'book/list_all.html', {'books_list': books_list})

@login_required(login_url='authentication:login')
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book/detail.html', {'book': book})

@login_required(login_url='authentication:login')
def create(request):
    if request.user.role != 1:
        return redirect('authentication:denied')
    if request.method == 'POST':
        form = BookCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book:list_all')
    else:
        form = BookCreateForm()
    return render(request, 'book/create.html', {'form': form})

@login_required(login_url='authentication:login')
def update(request, book_id):
    if request.user.role != 1:
        return redirect('authentication:denied')
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookCreateForm(instance=book, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('book:list_all')
    else:
        form = BookCreateForm(instance=book)
    return render(request, 'book/update.html', {'form': form})

@login_required(login_url='authentication:login')
def delete(request, book_id):
    if request.user.role != 1:
        return redirect('authentication:denied')
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('book:list_all')