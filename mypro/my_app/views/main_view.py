from django.shortcuts import render,redirect,get_object_or_404
from ..models import Employee

def index(request):
    empData = Employee.objects.all()
    return render(request, 'page/index.html',{'data':empData})

def createdemployee(request):
    errors = {}
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        salary = request.POST.get('salary')

        if not fullname:
            errors['fullname'] = 'fullname is required'
        
        if not email:
            errors['email'] = 'email is required'

        elif Employee.objects.filter(email = email):
            errors['email'] = 'email already exist add another'


        if not phone:
            errors['phone'] = 'phone number is required'

        if not salary:
            errors['salary'] = 'slary reqiuired'
    
        if not errors:
            data = Employee.objects.create(
                fullname = fullname,
                email = email,
                address = address,
                phone = phone,
                salary = salary
            )
            data.save()
            return redirect('index')
        else:
            return render(request, 'page/createdemployee.html', {'error':errors})

    return render(request, 'page/createdemployee.html')

def edit(request, id):
    # empdata = get_object_or_404(Employee, id)
    empdata = Employee.objects.get(id=id)
   
    if request.method == 'POST':
        empdata.fullname = request.POST.get('fullname')
        empdata.email = request.POST.get('email')
        empdata.phone= request.POST.get('phone')
        empdata.address = request.POST.get('address')
        empdata.salary = request.POST.get('salary')

        empdata.save()
        return redirect('index')

    return render(request, 'page/edit.html',{"empdata":empdata})


def update(request):
    return render(request, 'page/update.html')
