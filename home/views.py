from django.shortcuts import render,redirect
from .forms import ExpenseForm,LoginForm,RegisterForm
from .models import Expense
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
# Create your views here.
def home(request):
    return render(request,'home.html')

def LoginView(request):
    if request.method=='POST':
        form=LoginForm(request.POST)

        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']

            user=authenticate(username=username,
                              password=password)

            if user is not None:
                login(request,user)
                return redirect('home')
    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form})

def RegisterView(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)

        if form.is_valid():
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']

            user=User.objects.create_user(username=username,
                                          email=email,
                                          password=password)

            if user is not None:
                return render('login.html')
    else:
        form=RegisterForm()

    return redirect(request,'register.html',{'form':form})
class ListExpense(ListView):
    model=Expense
    template_name='list_expense.html'
    context_object_name='expenses'

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

class CreateExpense(CreateView):
    model=Expense
    template_name='create_expense.html'
    form_class=ExpenseForm
    success_url=reverse_lazy('list')

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

class UpdateExpense(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    model=Expense
    form_class=ExpenseForm
    template_name='create_expense.html'
    success_url=reverse_lazy('list')

    permission_required='home.change_expense'

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)


class DeleteExpense(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    model=Expense
    template_name='delete_expense.html'
    success_url=reverse_lazy('list')

    permission_required='home.delete_expense'

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)