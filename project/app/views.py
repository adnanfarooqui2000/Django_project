from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    return render(request,'register.html')
   
def login(request):
    if request.method=='POST':
        email1=request.POST.get('email')
        password1=request.POST.get('password')
        # print(email,password)
        name=request.COOKIES['name']
        email=request.COOKIES['email']
        contact=request.COOKIES['contact']
        password=request.COOKIES['password']
        if email1==email:
            if password1==password:
                data={'name':name,
                      'email':email,
                      'contact':contact,
                      'password':password
                      }
                return render(request,'dashboard.html',data)
            else:
                msg='email id and password not matched'
                return render(request,'login.html',{'msg':msg})
        else:
            msg='email id not register'
            return render(request,'login.html',{'msg':msg})
    else:
        return render(request,'login.html')
def logout(request):
    response =render(request,'home.html')
    response.delete_cookie('name')
    response.delete_cookie('email')
    response.delete_cookie('contact')
    response.delete_cookie('password')    
    return response

def dashboard(request):
    return render(request,'dashboard.html')


def register_Data(request):
    print(request.method)
    # print(request.POST)
    cstoken=request.POST.get('csrfmiddlewaretoken')
    name=request.POST.get('name')
    email=request.POST.get('email')
    contact=request.POST.get('contact')
    password=request.POST.get('password')

    print(cstoken)
    print(name)
    print(email)
    print(contact)
    print(password)
    response=render(request,'login.html')
    response.set_cookie('name',name)
    response.set_cookie('email',email)
    response.set_cookie('contact',contact)
    response.set_cookie('password',password)
    return response