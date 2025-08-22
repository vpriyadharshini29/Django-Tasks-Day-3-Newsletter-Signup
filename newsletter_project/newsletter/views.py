from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SubscriberForm, ManualSubscriberForm
from .models import Subscriber

def signup(request):
    if request.method == "POST":
        form = SubscriberForm(request.POST)  # using ModelForm
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for subscribing!")
            return redirect('signup')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = SubscriberForm()

    return render(request, 'newsletter/signup.html', {'form': form})


def manual_signup(request):
    if request.method == "POST":
        form = ManualSubscriberForm(request.POST)
        if form.is_valid():
            Subscriber.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email']
            )
            messages.success(request, "Subscribed successfully with manual form!")
            return redirect('manual_signup')
        else:
            messages.error(request, "Please fix the errors.")
    else:
        form = ManualSubscriberForm()

    return render(request, 'newsletter/signup.html', {'form': form})
