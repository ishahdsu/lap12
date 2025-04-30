from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Book
from django.db.models import Q
from django.db.models import Count, Sum, Avg, Max, Min


def index(request):
    return render(request, "bookmodule/index.html")
 
def list_books(request):
    return render(request, 'bookmodule/list_books.html')
 

 
def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')


def index2(request, val1=0):
    try:
        val1 = int(val1)  
        return HttpResponse(f"value1 = {val1}")
    except ValueError:
        return HttpResponse("Error, expected val1 to be an integer")
    
def viewbook(request, bookId):
    # assume that we have the following books somewhere (e.g. database)
    book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
    book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
    targetBook = None
    if book1['id'] == bookId: targetBook = book1
    if book2['id'] == bookId: targetBook = book2
    context = {'book':targetBook} # book is the variable name accessible by the template
    return render(request, 'bookmodule/one_book.html', context)


def links(request):
    return render(request, 'bookmodule/links.html')


def formatting(request):
    return render(request, 'bookmodule/formatting.html')

def listing(request):
    return render(request, 'bookmodule/listing.html')


def tables(request):
    return render(request, 'bookmodule/tables.html')

def search(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')

        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): contained = True
            if not contained and isAuthor and string in item['author'].lower():contained = True
            
            if contained: newBooks.append(item)
        return render(request, 'bookmodule/bookList.html', {'books':newBooks})
    return render(request, 'bookmodule/search.html')


def __getBooksList():
    book1 = Book(title = 'Continuous Delivery', author = 'J.Humble and D. Farley',price=120, edition = 3)
    book1.save()
    book2 = Book(title = 'Reversing: Secrets of Reverse Engineer', author = 'E.Eilam',price=97, edition = 2)
    book2.save()
    book3 = Book(title = 'The Hundred-Page Machine Learning Book', author = 'Andriy Burkov',price=100, edition = 4)
    book3.save()
    return [book1, book2, book3]

def book(request):
    return render(request, 'bookmodule/bookList.html',{'books':__getBooksList()})


def simple_query(request):
    mybooks=Book.objects.filter(title__icontains='and') # <- multiple objects
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})


def complex_query(request):
    mybooks=books=Book.objects.filter(author__isnull = False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10]
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')
    

def task1(request):
    mybooks=books=Book.objects.filter(Q(price__lte = 80)&Q(price__gt = 0) )
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')
    
def task2(request):
    mybooks=books=Book.objects.filter(Q(edition__gt = 3)&Q(price__gt = 0) &(Q(title__icontains = 'co')|Q(author__icontains = 'co')))
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')
    
def task3(request):
    mybooks=books=Book.objects.filter(~Q(edition__gt = 3)&Q(price__gt = 0) &(~Q(title__icontains = 'co')&~Q(author__icontains = 'co')))
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')

def task4(request):
    mybooks=books=Book.objects.all().order_by('title')
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')
    
def task5(request):
    mybooks = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    if len(mybooks)>=1:
        return render(request, 'bookmodule/task5.html', {'stats': mybooks})
    else:
        return render(request, 'bookmodule/index.html')
    

def list_books_part1(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/lab10_part1/lap10_listbooks.html', {'books': books})

def add_book_part1(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        edition = request.POST.get('edition')
        obj = Book(title=title, author=author, price=price, edition=edition)
        obj.save() 

        return redirect('list_books_part1')
    return render(request, 'bookmodule/lab10_part1/lap10_addbook.html')

def edit_book_part1(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.price = request.POST.get('price')
        book.edition = request.POST.get('edition')
        book.save()
        return redirect('list_books_part1')
    return render(request, 'bookmodule/lab10_part1/lab10_editbook.html', {'book': book})

def delete_book_part1(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books_part1')
    return render(request, 'bookmodule/lab10_part1/lab10_deletebook.html', {'book': book})

from .forms import BookForm

def list_books_part2(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/lab10_part2/listbooks_p2.html', {'books': books})


def add_book_part2(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books_part2')
    else:
        form = BookForm()
    return render(request, 'bookmodule/lab10_part2/addbook_p2.html', {'form': form})

def edit_book_part2(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books_part2')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookmodule/lab10_part2/editbook_p2.html', {'form': form, 'book': book})


def delete_book_part2(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books_part2')
    return render(request, 'bookmodule/lab10_part2/deletebook_p2.html', {'book': book})

