from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name= "books.index"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('html5/links/', views.links, name='links'),
    path('html5/text/formatting', views.formatting, name='formatting'),
    path('html5/listing', views.listing, name='listing'),
    path('html5/tables', views.tables, name='tables'),
    path('search/', views.search, name='search'),
    path('book/', views.book, name='book'),
    path('simple/query', views.simple_query, name='simple_query'),
    path('complex/query', views.complex_query, name='complex_query'),
    path('lab8/task1', views.task1, name='task1'),
    path('lab8/task2', views.task2, name='task2'),
    path('lab8/task3', views.task3, name='task3'),  
    path('lab8/task4', views.task4, name='task4'),  
    path('lab8/task5', views.task5, name='task5'),  
    
    path('lab10_part1/listbooks', views.list_books_part1, name='list_books_part1'),
    path('lab10_part1/addbook', views.add_book_part1, name='add_book_part1'),
    path('lab10_part1/editbook/<int:id>', views.edit_book_part1, name='edit_book_part1'),
    path('lab10_part1/deletebook/<int:id>', views.delete_book_part1, name='delete_book_part1'),

    path('lab10_part2/listbooks', views.list_books_part2, name='list_books_part2'),
    path('lab10_part2/addbook', views.add_book_part2, name='add_book_part2'),
    path('lab10_part2/editbook/<int:id>', views.edit_book_part2, name='edit_book_part2'),
    path('lab10_part2/deletebook/<int:id>', views.delete_book_part2, name='delete_book_part2'),

    





]

 
