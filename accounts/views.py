from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        
        # using ORM we can push data into database.
        if password1==password2:
            # checking if user already exists.
            if User.objects.filter(username=username).exists():
               messages.info(request,'Username already taken.')
               return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already taken')
                return redirect('register')
            else:
                # all labels are already available in models object of django.
                user  = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                
                return redirect('login')
        else:
            messages.info(request,'passwords are not matching')
            return redirect('register')
        # after registration we want to call home page.
        return redirect("/")
    else:
        return render(request,'register.html')
   
def login(request):
    if request.method=='POST':
        # fetching data
        username=request.POST['username']
        password=request.POST['password']
        
        # authenticate
        user = auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            # after authnticate we redirect it tp home page
            return redirect("/")
        else:
            messages.info(request,'invalid credentials.')
            # gain call same page.
            return redirect('login')
    else:
        return render(request,'login.html')
     
def logout(request):
    auth.logout(request)
    # after logout call home page
    return redirect("/")

def home(request):
     return render(request,'index.html')
 
def about(request):
     return render(request,'about.html')
