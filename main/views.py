from django.shortcuts import render, redirect
from .models import Profile
from django.contrib import messages

# Home.
def home(request):
	return render(request, 'main/home.html', {})

def profiles(request):
	if request.user.is_authenticated:
		profiles = Profile.objects.exclude(user=request.user)
		return render(request, 'main/profiles.html', {'profiles': profiles})
	else:
		messages.warning(request, ('You are not logged in!'))
		return redirect('home')

def profile(request, id):
	if request.user.is_authenticated:
		profile = Profile.objects.get(user_id=id)
		return render(request, 'main/profile.html', {'profile': profile})
	else:
		messages.warning(request, ('You are not logged in!'))
		return redirect('home')