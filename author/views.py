from django.shortcuts import render, redirect, get_object_or_404
from .models import Author
from .forms import AuthorForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='authentication:login')
def authors_list(request):
    authors = Author.get_all()
    if request.method == 'POST':
        if request.user.role != 1:
            return redirect('authentication:denied')
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author:list')
    else:
        form = AuthorForm()
    return render(request, 'author/author.html', {'authors': authors,
                                                  'form': form})


@login_required(login_url='authentication:login')
def author_detail(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    books = author.books.all()
    return render(request, 'author/detail.html', {'author': author,
                                                  'books': books})


@login_required(login_url='authentication:login')
def update_author(request, author_id):
    if request.user.role != 1:
        return redirect('authentication:denied')
    author = get_object_or_404(Author, id=author_id)
    if request.POST:
        form = AuthorForm(instance=author, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('author:list')
    else:
        form = AuthorForm(instance=author)
        authors = Author.get_all()
    return render(request, 'author/author.html', {'form': form,
                                                  'authors': authors})


@login_required(login_url='authentication:login')
def delete_author(request, author_id):
    if request.user.role != 1:
        return redirect('authentication:denied')
    author = get_object_or_404(Author, id=author_id)
    author.delete()
    return redirect('author:list')