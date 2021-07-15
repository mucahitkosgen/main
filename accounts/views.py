from django.shortcuts import render, redirect
from .forms import signin
from django.contrib.auth import  authenticate, login

# Create your views here.

def sign_in(request):
    form = sign_in(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username = username, password = password)
        login(request,user)
        return redirect('index')
    return render(request, 'T3/light/sign-in.html', {form :'form'})