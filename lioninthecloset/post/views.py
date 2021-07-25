from django.shortcuts import render, redirect, get_object_or_404
from .models import Combination, Item
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.utils import timezone

def closet_view(request):
    items = Item.objects.all()
    combis = Combination.objects.all()
    return render(request, 'closet.html', {'items': items, 'combis': combis})

def add_to_combi(request, index, pk):
    if request.method == 'POST':
        combis = get_object_or_404(Combination, pk = index)
        combis.Item.add(pk)
        
    return redirect('combination_detail', index = index)

def combination_detail(request, index):
    combis = get_object_or_404(Combination, pk = index)
    item_list = Item.objects.all
    return render(request, 'combination_detail.html', {'combis':combis, 'item_list':item_list})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)
            return redirect("home")
        return redirect("login")
    else:        
        form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})


def logout_view(request):
    logout(request)
    return redirect("home")

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            print("valid")
            user = form.save()
            login(request, user)
            return redirect('home')
        return redirect('signup')
    else:
        form = RegisterForm()
        return render(request, 'signup.html', {'form':form})

def home(request):
    return render(request, 'home.html')

def new(request):
    form = ItemForm()
    return render(request, 'create.html', {'form':form})

def create(request):
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid:
            new_item = form.save(commit=False)
            new_item.date = timezone.now()
            new_item.save()
            for img in request.FILES.getlist('imgs'):
                image = Image()
                image.post = post
                image.file = img
                image.save()
            return redirect('item_detail', index = new_item.id)
        return redirect('closet')
    else:
        form = ItemForm()
        return render(request, 'create.html', {'form':form})

def edit(request, id):
    re_item = Item.objects.get(id = id)
    return render(request, 'edit.html', {'item':re_item})

def item_detail(request, index):
    item = Item.objects.get(id=index)
    return render(request, 'item_detail.html', {'item':item})
