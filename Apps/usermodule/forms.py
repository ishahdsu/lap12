from django import forms
from .models import student , address ,student2 , address2 ,Photo

class StudentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ['name', 'age', 'address']
    
    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['address'].queryset = address.objects.all()
        self.fields['address'].label_from_instance = lambda obj: obj.city




class Student2Form(forms.ModelForm):
    class Meta:
        model = student2
        fields = ['name', 'age', 'addresses']

    name = forms.CharField(label="Student Name", required=True)
    age = forms.IntegerField(label="Age", required=True, min_value=0)
    addresses = forms.ModelMultipleChoiceField(
        label="Addresses",
        queryset=address2.objects.all().order_by("city"),
        widget=forms.CheckboxSelectMultiple()
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  

from .models import Photo

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'image']





  