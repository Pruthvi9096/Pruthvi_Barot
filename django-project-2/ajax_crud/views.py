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
    print("-----inside  view-----",request.method)
    data = {}
    if request.method == 'POST':
        form = BookForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            data.update({'form_is_valid':True})
            books = Book.objects.all()
            data.update({'html_book_list': render_to_string('partial_book_list.html', {
                'books': books
            })
            })
            # return redirect(reverse('book_list'))
        else:
            data.update({'form_is_valid':False})
        return JsonResponse(data)
    else:
        form = BookForm()
    context = {'form': form}
    data.update({'html_form':render_to_string('partial_book_create.html',
        context,
        request=request,
        )})
    return JsonResponse(data)