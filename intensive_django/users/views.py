from django.contrib.auth import login
from django.shortcuts import redirect, render, get_object_or_404

from users.forms import SignUpForm, ProfileForm
from users.models import Account


def sign_up(request):
    form = SignUpForm(request.POST or None)
    context = {
        'form': form,
    }

    if request.method == 'POST' and form.is_valid():
        user = Account.objects.create_user(**form.cleaned_data)

        login(request, user)

        return redirect('homepage:home')

    return render(request, 'users/signup.html', context)


def user_list(request):
    context = {
        'users': Account.objects.values('id', 'email'),
    }
    return render(request, 'users/user_list.html', context)


def user_detail(request, pk):
    context = {
        'user': get_object_or_404(Account, pk=pk),
    }
    return render(request, 'users/user_detail.html', context)


def profile(request):
    if request.user.is_authenticated:
        user = request.user

        form = ProfileForm(request.POST or {
            'last_name': user.last_name,
            'first_name': user.first_name,
            'birthday': str(user.birthday),
        } or None)

        context = {
            'form': form,
        }

        if request.method == 'POST' and form.is_valid():
            print(form.cleaned_data['birthday'], form.cleaned_data['first_name'])

            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.birthday = form.cleaned_data['birthday']

            user.save()

            return redirect('users:profile')

        return render(request, 'users/profile.html', context)

    return redirect('homepage:home')
