from django.shortcuts import render,get_object_or_404
from library.models import *
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from library.forms import RenewBookForm
import datetime

@permission_required('library.can_mark_returned')
def renew_book_librarian(request,pk):
	book_instance = get_object_or_404(BookInstance,pk=pk)

	if request.method == 'POST':
		form = RenewBookForm(request.POST)

		if form.is_valid():
			book_instance.due_back = form.cleaned_data['renewal_date']
			book_instance.save()
			return HttpResponseRedirect(reverse('all-borrowed'))
	else:
		proposed_renewal_date =  datetime.date.today() + datetime.timedelta(weeks=3)
		form = RenewBookForm(initial={'renewal_date':proposed_renewal_date})
		context = {
			'form':form,
			'book_instance':book_instance,
		}
		return render(request,'book_renew_librarian.html',context)

@login_required(login_url='/login/')
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default.    
    num_authors = Author.objects.count()

    #session example
    num_visit = request.session.get('num_visit',0)
    request.session['num_visit'] = num_visit + 1
    
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visit':num_visit
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
	model = Book
	# context_object_name = 'my_book_list'   # your own name for the list as a template variable
	queryset = Book.objects.all()
	# print("-------------",queryset)
	# queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
	template_name = 'book_list.html'  # Specify your own template name/location
	paginate_by = 10

class BookDetailView(generic.DetailView):
	model = Book
	template_name = 'book_detail.html'
	# queryset = get_object_or_404(Book,pk=p)

class AuthorListView(generic.ListView):
	model = Author
	template_name = 'author_list.html'
	paginate_by = 10

class AuthorDetailView(generic.DetailView):
	model = Author
	template_name = 'author_detail.html'

class LoanedBooksByUserListView(generic.ListView):
	model = BookInstance
	template_name = 'bookinstance_list_borrowed_user.html'
	paginate_by = 10

	def get_queryset(self):
		return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')


class LoanedBooksAllListView(PermissionRequiredMixin, generic.ListView):
    """Generic class-based view listing all books on loan. Only visible to users with can_mark_returned permission."""
    model = BookInstance
    permission_required = 'library.can_mark_returned'
    template_name = 'bookinstance_list_borrowed_all.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').order_by('due_back')

class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'
    # initial = {'date_of_death': '05/01/2018'}

class AuthorUpdate(UpdateView):
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']

class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('authors')

class BookCreate(CreateView):
    model = Book
    fields = '__all__'

class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books')

class BookInstCreate(CreateView):
    model = BookInstance
    fields = '__all__'

class BookInstUpdate(UpdateView):
    model = BookInstance
    fields = '__all__'

class BookInstDelete(DeleteView):
    model = BookInstance
    success_url = reverse_lazy('books')

class BookInstListView(generic.ListView):
	model = BookInstance
	template_name = 'bookinstance_list.html'
	paginate_by = 10