from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from .forms import RegisterForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, authenticate


# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/restaurants/welcome")  # for now, returns to homepage when registration is successful
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form":form})