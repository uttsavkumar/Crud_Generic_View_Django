from django.shortcuts import render,redirect
from django.views.generic import ListView,DeleteView,CreateView,UpdateView,FormView,View
from .models import StudentRecord
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password
from django.urls import reverse_lazy
from django.contrib.auth.models import User
class StudentView(ListView):

    model = StudentRecord
    template_name = './home.html'
    
    def get_queryset(self):
       search = self.request.GET.get('search',"")
       return StudentRecord.objects.filter(name__icontains=search) 

class StudentDelete(DeleteView):
    model = StudentRecord
    success_url = reverse_lazy('home')
    template_name='./delete.html'

class StudentInsert(CreateView):
    
    template_name = './insert.html'
    model = StudentRecord
    fields =  '__all__'
    success_url = reverse_lazy('home')

class StudentEdit(UpdateView):

    template_name = './insert.html'
    model = StudentRecord
    fields =  '__all__'
    success_url = reverse_lazy('home')


class LoginVIew(FormView):
    template_name = './login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')  

    def post(self,req):
        username = req.POST.get('username')
        password = req.POST.get('password')

        user = authenticate(username=username,password=password)
        if user is not None :
            login(req,user=user)
            return redirect('home')
        else:
            return redirect('login')
        

class LogoutView(View):
    def get(self,req):
        logout(req)
        return redirect('home')
    
class Signup(CreateView):
    template_name = './register.html'
    model = User
    fields =  ['first_name','last_name','email','username','password']
    success_url = reverse_lazy('login')

    def form_valid(self,form):
        user = form.save(commit=False)
        user.password = make_password(form.password)
        user.save()
        return super().form_valid(form)
