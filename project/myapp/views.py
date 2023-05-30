from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, logout, authenticate
from .models import customers
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
import jwt


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        ob = customers.objects.all()
        d = {"obj": ob}
        return render(request, 'homepage.html', d)
    else:
        return redirect("/")


def data(request):
    if request.method == 'GET':
        return HttpResponse("You are trying to access the page with 'GET' method")
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password1 = request.POST['p1']
        password2 = request.POST['p2']
        age = request.POST['age']
        if password1 == password2:
            obj = customers()
            obj.name = name
            obj.email = email
            obj.age = age
            obj.password = password2
            try:
                obj.save()
                return redirect("/")
            except:
                return HttpResponse("Data not saved")
        else:
            return HttpResponse("Password not matched")


def delete(request, id):
    obj = customers.objects.get(pk=id)
    obj.delete()
    return redirect("/")


def update(request, id):
    if request.method == 'POST':
        mid = request.POST['id']
        ob = customers.objects.get(pk=mid)
        ob.name = request.POST['name']
        ob.email = request.POST['email']
        ob.password = request.POST['p1']
        ob.age = request.POST['age']
        try:
            ob.save()
            return redirect("/")
        except:
            return HttpResponse("Data not saved")
    obj = customers.objects.get(pk=id)
    d = {"obj": obj, "id": id}
    return render(request, "update.html", d)


def signUp(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        us = User.objects.create_user(username=name, email=email, password=password, is_active=False)
        try:
            us.save()
            enc=jwt.encode(payload={"myId":str(us.pk)},key='secret',algorithm="HS256")
            link = request.scheme + "://" + request.META["HTTP_HOST"] + "/activate/" + str(enc) + "/"
            em = EmailMessage("Info", "Thank you for the registration account " + link, "rizwanali96960@gmail.com", [email])
            em.send()
            return redirect('/')
        except:
            return render(request, 'signup.html', {'mes': "some error accorded try again later"})
    return render(request, "signup.html")


def loginn(request):
    if request.method == "POST":
        email = request.POST["loginEmail"]
        password = request.POST["loginpassword"]
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("homePage/")
        else:
            return render(request, "login.html", {"mes": "Wrong Email or Password"})
    if request.user.is_authenticated:
        return redirect("homePage/")
    else:
        return render(request, "login.html")


def logoutt(request):
    logout(request)
    return redirect("/")


def activate(request, id):
    dec=jwt.decode(id,key='secret',algorithms=["HS256"])
    u = User.objects.get(pk=int(dec['myId']))
    u.is_active = True
    u.save()
    return redirect("/")
