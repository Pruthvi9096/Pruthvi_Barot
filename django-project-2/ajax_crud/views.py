from django.shortcuts import render,redirect
from .models import Book
from django.http import JsonResponse
from django.template.loader import render_to_string
from .forms import BookForm
from django.urls import reverse


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def book_create(request):
    data = {}
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            data.update({'form_is_valid':True})
            return redirect(reverse('book_list'))
        else:
            data.update({'form_is_valid':False})
    else:
        form = BookForm()
    context = {'form': form}
    data.update({'html_form':render_to_string('partial_book_create.html',
        context,
        request=request,
        )})
    return JsonResponse(data)