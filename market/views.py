from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateMarketForm, MarketUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = CreateMarketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Вход')
    else:
        form = CreateMarketForm()
    context = {
        'form': form,
    }
    return render(request, 'market/register.html', context)

@login_required(login_url='Вход')
def profile(requset):
    return render(requset, 'market/profile.html')

@login_required(login_url='Вход')
def profile_update(request):
    if request.method == 'POST':
        u_form = MarketUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('Профиль')
    else:
        u_form = MarketUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'market/profile_update.html', context)
