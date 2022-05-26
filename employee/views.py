from django.shortcuts import render
from django.views import View

class EmployeeView(View):
    template_name = 'employee/index.html'
    name = 'employee'

    def get(self, request):
        context = {'name': self.name}
        return render(request,self.template_name, context=context)

class HomeView(View):
    template_name = 'home/index.html'
    name = 'home'
    def get (self, request):
        context = {'name': self.name}
        return render(request,self.template_name, context=context)

class SalaryView(View):
    template_name = 'salary/salary.html'
    name = 'salary'
    def get (self, request):
        context = {'name': self.name}
        return render(request,self.template_name, context=context)

class LoginView(View):
    template_name = 'auth/login.html'
    name = 'login'
    def get (self, request):
        
        context={
            'name': self.name
        }

        return render(request, self.template_name, context=context)


