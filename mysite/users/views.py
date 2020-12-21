from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  # for just momentary messages
# Create your views here.


# generally we use normal GET request ,but we want the data entered so we will use 'POST' request
def register(request):
    if request.method == 'POST':
        # instanciate the form with POST data.
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # to get the cleaned data obtained from the form in python types
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            # BUG: this doesn't redirect to the given 'about-page'
            # return redirect('about-page')
    else:
        form = UserCreationForm()

    return render(request, 'users/register.html', {'form': form})
