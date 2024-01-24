from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, UserProfileForm

def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('login')
    else:
        user_form = RegistrationForm()
        profile_form = UserProfileForm()

    return render(request, 'registration.html', {'user_form': user_form})

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return "USER NOT EXISTS",400

    return render(request, 'login.html')

@login_required
def home(request):
    user_role = request.user.userprofile.role
    # Redirect to the appropriate page based on user role currently handled all the users to same page
    if user_role == 'student':
        return render(request, 'user_role.html')
    elif user_role == 'staff':
        return render(request, 'user_role.html')
    elif user_role == 'admin':
        return render(request, 'user_role.html')
    elif user_role == 'editor':
        return render(request, 'user_role.html')

