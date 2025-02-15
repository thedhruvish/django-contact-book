from django.shortcuts import render,redirect
from .models import User,Contact

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        login_user = User.objects.filter(email=email, password=password)

        if login_user.count() == 1:
            request.session['email'] = login_user.get().email
            request.session['name'] = login_user.get().name
            redirect('/dashboard/')
        else:
            errorMSG = 'Your Email and Password is Wrong'
            return render(request,'login.html',{"msg":errorMSG})
                
    return render(request,'login.html')


def register_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        new_user = User(
            name=name,
            email=email,
            password=password
        )
        new_user.save()
        redirect('/login/')
    return render(request,'register.html')



def dashboard_view(request):
    return render(request,'dashboard.html')


def add_contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        gender = request.POST.get("gender")
        city = request.POST.get("city")
        c_number =request.POST.get('c_number')
        address = request.POST.get('address')

        new_contact = Contact(
            owner=request.session['email'],
            name=name,
            email=email,
            gender=gender,
            city=city,
            c_number = c_number,
            address = address
        )
        new_contact.save()
        return redirect('/view_contact/')
    return render(request,'add_contact.html')



def view_contact_view(request):
    contacts = Contact.objects.filter(owner=request.session['email'])
    return render(request,'view_contact.html',{'data':contacts})


def change_password_view(request):
    if request.method == 'POST':
        password = request.POST.get('password')

        checkUser = User.objects.filter(email=request.session['email'],password=password)

        if checkUser.count() == 1:
            return render(request,'new_password.html')
        else:
            redirect('/logout/')
    return render(request,'change_password.html')

def set_new_password(request):
    if request.method == 'POST':
        new_password = request.POST.get('n_password')
        curr_new_password = request.POST.get('curr_new_password')

        oldpassword = User.objects.filter(email=request.session['email']).get().password

        if new_password == curr_new_password and oldpassword != new_password:
            update = User.objects.filter(email=request.session['email']).update(password=new_password)
            return redirect('/logout/')
        else:
            msg = "Enter New Password"
            return render(request,'new_password.html',{'error':msg})
    return render(request,'new_password.html')

def edit_contact_view(request,id):
    contact = Contact.objects.get(id=id)
    return render(request,'add_contact.html',{'data':contact})

def update_contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        gender = request.POST.get("gender")
        city = request.POST.get("city")
        c_number =request.POST.get('c_number')
        address = request.POST.get('address')
        id = request.POST.get('id')

        update = Contact.objects.filter(id=id).update(
            name=name,
            email=email,
            gender=gender,
            city=city,
            c_number = c_number,
            address=address
        )
        return redirect("/view_contact/")



def logout_view(request):
    del request.session['email']
    del request.session['name']
    return redirect('/login/')

