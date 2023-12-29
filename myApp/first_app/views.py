from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    return render(request, 'first_app/index.html')

def about(request):
    return render (request, 'first_app/about.html')

def contact(request):
    return render(request, 'first_app/contact.html')

def projects(request):
    newDate = datetime.datetime.now()
    my_obj = {
        'my_date': newDate,
        'age': 25,
        'name': 'rahim',
        'name1': 'ka ri m',
        'no_name': '',
        'have_name': 'sakib',
        'symbol_1': '<',
        'sizeOfFile': 12345678,
        'arr' : [
            {'name': 'karim', 'age': 32, 'numbers': 34},
            {'name': 'rarim', 'age': 29, 'numbers': 43},
            {'name': 'sakib', 'age': 26, 'numbers': 42},
            {'name': 'rakib', 'age': 21, 'numbers': 12},
            {'name': 'akib', 'age': 54, 'numbers': 54},
            {'name': 'nafis', 'age': 27, 'numbers': 67},
        ]
    }
    return render(request, 'first_app/projects.html', my_obj)