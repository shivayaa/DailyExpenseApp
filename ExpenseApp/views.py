from django.shortcuts import render,redirect,HttpResponse
from .models import User,Income,Expense
from .forms import UserForm,IncomeForm,ExpenseForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def home(request):
    uname=request.session.get('userName')
    uid=request.session.get('userId')
    incl=Income.objects.filter(user_id=uid)
    totalIncome=0
    for i in incl:
        totalIncome=totalIncome+i.income 

    print("Total Income is----------->",totalIncome)
    totalExpense=0
    exlist=Expense.objects.filter(User_id=uid)
    for i in exlist:
        totalExpense=totalExpense+i.expense 

    print('Total Expense is-------->',totalExpense)
    totalBalance=totalIncome-totalExpense
    d={"uname":uname,'bal':totalBalance}

    return render(request,'index.html',d)

def addUser(request):
    if request.method=='POST':
        f=UserForm(request.POST)
        f.save()
        return redirect("/")    
    else:
        f=UserForm
        return render(request,'form.html',{'form':f})

def addIncome(request):
    if request.method=='POST':
        f=IncomeForm(request.POST)
        f.save()
        return redirect("/")    
    else:
        f=IncomeForm
        return render(request,'form.html',{'form':f})

def addExpense(request):
    if request.method=='POST':
        f=ExpenseForm(request.POST) 
        f.save()
        return redirect("/")    
    else:
        f=ExpenseForm
        return render(request,'form.html',{'form':f}) 

def incomeList(request):
    uid=request.session.get('userId')
    incl=Income.objects.filter(user_id=uid)
    return render(request,'incomeList.html',{'ilist':incl})


def expenseList(request):
    uid=request.session.get('userId')
    exlist=Expense.objects.filter(User_id=uid)
    return render(request,'expenseList.html',{'ilist':exlist})

def userLogin(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        passw=request.POST.get('passw')
        user=authenticate(request,username=uname,password=passw)
        if user is not None:
            request.session['userId']=user.id
            request.session['userName']=uname 
            login(request,user)
            return redirect('/')

        else:
            return HttpResponse("<h1> Invalid User Or Password </h1>")

    else:
        return render(request,'login.html')

def userLogout(request):

    logout(request)
    return redirect('/')

def editProfile(request):
    
    uid=request.session.get('userId')
    u=User.objects.get(id=uid)
    if request.method=='POST':
        f=UserForm(request.POST,instance=u)
        f.save()
        return redirect("/")
    else:
        f=UserForm(instance=u)
        return render(request,'form.html',{'form':f})
