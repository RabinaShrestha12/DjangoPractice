from django.shortcuts import render,redirect,get_object_or_404
from ..models import Employee
from django.contrib.auth.models import User

def indexs(request):
    empData = Employee.objects.all()
    return render(request, 'page/indexs.html',{'data':empData})

def ind(request):
    return render(request, "ind.html")

def index(request):
    return render(request,'index.html')

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
        elif len(phone)<7 or len(phone)>15:
            errors['phone'] = '"Phone must contains less than 7 and more than 15 digits'

        if not salary:
            errors['salary'] = 'salary reqiuired'
    
        if not errors:
            data = Employee.objects.create(
                fullname = fullname,
                email = email,
                address = address,
                phone = phone,
                salary = salary
            )
            data.save()
            return redirect('indexs')
        else:
            return render(request, 'page/createdemployee.html', {'error':errors,'data': request.POST})

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
        return redirect('indexs')

    return render(request, 'page/edit.html',{"empdata":empdata})



def delete_data(request, emp_id):
    empt = Employee.objects.get(id = emp_id)
    empt.delete()
    return redirect('indexs')



