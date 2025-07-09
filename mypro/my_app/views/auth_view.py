from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

def loginpage(request):
    errors = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        password= request.POST.get('password')
        
        # auth_user  = User.objects.filter(email = email).exists(), filter used vaya ko sabai data haru used linxa or phase gardinxa tara get garo vana chayna matar linxa
        auth_user = User.objects.get(email = email)
        if auth_user:
         user = authenticate(request,username=auth_user.username,password=password)
        if user is not None:
            login(request, user) #session gererate garxa
            return redirect('index')
        else:
            errors['login_error'] ="username doesnot exists"
            return render(request, 'auth/loginpage.html')
    return render(request, 'auth/loginpage.html')

def register(request):
    errors = {}
    if request.method == 'POST':
        username= request.POST.get('username')
        email= request.POST.get('email')
        password= request.POST.get('password')
        confirm_password= request.POST.get('confirm_password')
       
        if password != confirm_password:
            errors['confirm_password'] = "Password doesn't match."

        if not username:
            errors['username'] = "Username is required"

        if not email:
            errors['email'] = "email is required"

        if not password:
            errors['password'] = "password i required"

        if not confirm_password:
            errors['confirm_password'] = "confirm password is required"

        if not errors:
            # user  = User.objects.create (
            #     username=username,
            #     email = email
            # )
            # user.set_password(password)#password hash or encripted
            # user.save()
            # return redirect('login')
        # yo code la chai password direct hase gardinxa
            user = User.objects.create_user(
            username = username,
            email = email,
            password = password,
            )
            user.save()
            return redirect('login')
        else:
            errors['errors'] = "failed to login "
            return render(request, 'auth/register.html',{'errors':errors})
    return render(request, 'auth/register.html')

def logout_user(request):
    logout(request)
    return redirect('index')