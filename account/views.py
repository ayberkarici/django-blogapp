from django.shortcuts import redirect, render
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.


def login_request(request):
    if request.user.is_authenticated:
        return redirect("home")
    
    
    if request.method == "POST": 
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(request, username = username, password = password)
    
        if user is not None: 
            login(request, user)
            return redirect("home")
        else:
            return render(request, "account/login.html", {
                "error" : "Username veya parola yanlış"
            })
        
    return render(request, "account/login.html")
    

def register_request(request):
    if request.user.is_authenticated:
        return redirect("home")
    
    if request.method == "POST":
        username = request.POST["username"]
        name = request.POST["name"]
        email = request.POST["email"]
        lastname = request.POST["lastname"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]
        
        register_details = {
            "username" : username,
            "name" : name, 
            "email" : email, 
            "lastname" : lastname,
        }
            
        if password == repassword:
            if User.objects.filter(username = username).exists():
                return render(request, "account/register.html", {"error" : "Bu kullanıcı adı alınmış"})
            else:
                if User.objects.filter(email = email).exists():
                    return render(request, "account/register.html", {"error" : "Bu Email kullanılıyor"})
                else:
                    user = User.objects.create_user(username = username, password = password, first_name = name, last_name = lastname, email = email)
                    user.save() # Yeni kullanıcıyı kayıt ediyoruz
                    return redirect("login")
        else: 
            return render(request, "account/register.html", {"error" : "Parolalar eşleşmiyor"})
        
    
    return render(request, "account/register.html")

def logout_request(request):
    logout(request)
    
    return render(request, "account/login.html")
