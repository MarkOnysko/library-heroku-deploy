from django.shortcuts import render, redirect, get_object_or_404
from .models import CustomUser
from .forms import RegistrationForm, UserUpdateForm, UsersChangePermissionsForm
from django.contrib.auth.decorators import login_required


def denial(request):
    return render(request, 'auth/denied.html')


def index(request):
    if request.user.is_authenticated:
        return redirect('book:list_all')
    return render(request, 'auth/index.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # new_user = form.save(commit=False)
            # new_user.set_password(form.cleaned_data['password'])
            # new_user.save()
            return redirect('authentication:reg_done')
    else:
        form = RegistrationForm()
    return render(request, 'auth/register.html', {'form': form})


def reg_done(request):
    return render(request, 'auth/registration_done.html')


@login_required(login_url='authentication:login')
def update(request, user_id):
    user_to_update = get_object_or_404(CustomUser, id=user_id)
    if request.method == "POST":
        form = UserUpdateForm(instance=user_to_update, data=request.POST)
        if form.is_valid():
            updated_user = form.save(commit=False)
            updated_user.set_password(form.cleaned_data['password2'])
            updated_user.save()
            return redirect('authentication:detail', user_id=user_id)
    else:
        form = UserUpdateForm(instance=user_to_update)
    return render(request, 'auth/update.html', {'form': form})


@login_required(login_url='authentication:login')
def change_permissions(request, user_id):
    if request.user.role != 1:
        return redirect('authentication:denied')
    user_to_update = get_object_or_404(CustomUser, id=user_id)
    if request.method == "POST":
        form = UsersChangePermissionsForm(instance=user_to_update, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('authentication:users_list')
    else:
        form = UsersChangePermissionsForm(instance=user_to_update)
        return render(request, 'auth/change_permissions.html', {"form": form})

@login_required(login_url='authentication:login')
def list_all(request):
    if request.user.role != 1:
        return redirect('authentication:denied')
    users = CustomUser.get_all()
    return render(request, 'auth/list.html', {'users': users})


@login_required(login_url='authentication:login')
def detail(request, user_id):
    if request.user.role != 1 and request.user.id != user_id:
        return redirect('authentication:denied')
    user_to_view = get_object_or_404(CustomUser, id=user_id)
    orders = user_to_view.order_set.all()
    return render(request, 'auth/detail.html', {'user_to_view': user_to_view,
                                                'orders': orders})


@login_required(login_url='authentication:login')
def delete(request, user_id):
    if request.user.id != user_id:
        return redirect('authentication:denied')
    user = get_object_or_404(CustomUser, id=user_id)
    user.delete()
    return redirect('authentication:deleted')


def deleted(request):
    return render(request, 'auth/deleted.html')
