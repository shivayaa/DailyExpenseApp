from django.contrib import admin
from django.urls import path
from .import views as v 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v.home),
    path('addUser',v.addUser),
    path('addIncome',v.addIncome),
    path('addExpense',v.addExpense),
    path('incomeList',v.incomeList),
    path('expenseList',v.expenseList),
    path('userLogin',v.userLogin),
    path('userLogout',v.userLogout),
    path('editProfile',v.editProfile),
]