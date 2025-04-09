from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.template import loader
from .forms import RegisterForm, AddPortfolioForm, SearchUserForm
from django.core.paginator import Paginator
from .models import Users, Works, Messages

# Create your views here.

def mainRender(request):
    return render(request, 'main.html') 
    
def loginRender(request):
    if request.method == "POST":
        loginform = AuthenticationForm(request, data=request.POST)
        if loginform.is_valid():
            user = loginform.get_user()
            login(request, user, backend='website_app.backends.EmailAuthBackend') #check with default backend
            return redirect('main_path')
    else:
        loginform = AuthenticationForm()
    return render(request, 'login.html', {'form': loginform})

def registRender(request):
    if request.method == "POST":
        registform = RegisterForm(request.POST)
        if registform.is_valid():
            user = registform.save(commit=False)
            user.set_password(registform.cleaned_data["password"])
            user.save()
            #also can create via signals.py
            Messages.objects.create(
                user = user,
                topic = "Welcome letter",
                message_text = "Hello, thank you for using our website! Hope it will be useful for you"
            )
            login(request, user, backend='django.contrib.auth.backends.ModelBackend') 
            return redirect('main_path')
    else:
        registform = RegisterForm()
    return render(request, 'register.html', {'form': registform})

def logoutView(request):
    logout(request)
    return redirect('main_path')

def usersRender(request):
    user = request.user
    messages = Messages.objects.all().filter(user=user).order_by('-date')
    searchform = SearchUserForm(request.GET or None)
    users_lists = Users.objects.all()
    if searchform.is_valid() and searchform.cleaned_data["query"]:
        query_text = searchform.cleaned_data["query"]
        users_lists = users_lists.filter(username__icontains=query_text)
    else:
        query_text = ''

    paginator = Paginator(users_lists, 35)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'users.html', {'page_obj' : page_obj,
                                          'form' : searchform,
                                          'query' : query_text,
                                          'messages' : messages})

User = get_user_model()
def profileRender(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'profile.html', {'user' : user})

def addportfolioRender(request, user_id):
    if request.user.id != user_id:
        return redirect('main_path')
    if request.method == "POST":
        portfolioform = AddPortfolioForm(request.POST, request.FILES, user=request.user)
        if portfolioform.is_valid():
            portfolio = portfolioform.save(commit=False)
            portfolio.user = request.user
            portfolio.save()
            return redirect('main_path')
    else:
        portfolioform = AddPortfolioForm(user=request.user)
        user = get_object_or_404(User, id=user_id)
    return render(request, 'addportfolio.html', {'form' : portfolioform,
                                                 'user' : user})

    



