from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    title = forms.CharField(
        max_length=100,
        required=True,
        label="Title",
        widget=forms.TextInput(attrs={
            'placeholder': '',
            'class': "mycssclass",
            'id': 'jsID'
        })
    )

    author = forms.CharField(
        max_length=100,
        required=True,
        label="Author",
        widget=forms.TextInput(attrs={
            'class': "mycssclass",
            'id': 'jsID2'
        })
    )

    price = forms.DecimalField(
        required=True,
        label="Price",
        initial=0,
        widget=forms.NumberInput()

    )

    edition = forms.IntegerField(
        required=True,
        label="Edition",
        initial=0,
        widget=forms.NumberInput()
    )

    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'edition']
