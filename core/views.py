from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from .forms import CustomUserCreationForm
from .models import Book, IssuedBook
from django.contrib.auth.decorators import login_required
def home(request):
    return render(request,'core/index.html')

def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('view_issued')
        else:
            print('Error')
    return render(request,'core/login.html')

def sign_up(request):
    form = CustomUserCreationForm(request.POST or None)
    if request.method =='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('view_book')
        else:
            print('Error')

    return render(request,'core/register.html',{'form':form})

@login_required(login_url='sign_in')
def view_books(request):
    books = Book.objects.all()
    context = {'books':books}
    return render(request,'core/view_books.html',context)

@login_required(login_url='sign_in')
def view_issued_books(request):
    books = IssuedBook.objects.filter(student_id = request.user)
    context = {'books':books}
    return render(request,'core/view_issued.html',context)

@login_required(login_url='sign_in')
def delete_issued_book(request, pk):
    books = IssuedBook.objects.get(id=pk)
    books.delete()
    return redirect("view_issued")

@login_required(login_url='sign_in')
def add_to_issue(request,pk):
    book = Book.objects.get(id=pk)
    issue_book = IssuedBook.objects.create(
        student_id = request.user,
        book_id = book,
    )
    issue_book.save()
    return redirect('view_issued')

def sign_out(request):
    logout(request)
    return redirect('home')

def about(request):
    return render(request,'core/about.html')

def test(request):
    return HttpResponse('Yello')