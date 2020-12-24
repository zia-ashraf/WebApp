from django.shortcuts import render, redirect

# from django.contrib.auth.forms import UserCreationForm no more using this.
from django.contrib import messages  # for just momentary messages
# Create your views here.
from polls import views, urls
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# generally we use normal GET request ,but we want the data entered so we will use 'POST' request


def register(request):
    if request.method == 'POST':
        # instanciate the form with POST data.
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # to get the cleaned data obtained from the form in python types
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account created for {username}! You are now able to login')
            # BUG: this doesn't redirect to the given 'about-page'
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required  # decorator-adds functionality to an existing function
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)
