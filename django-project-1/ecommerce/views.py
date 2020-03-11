from django.shortcuts import render,redirect
from django.http import *
from ecommerce.models import Product,Category
from ecommerce.forms import CreateProductForm,CreateCategoryForm

def display_all_products(request):
	products = Product.objects.all()
	context = {
		'products':products
	}
	return render(request,"product_index.html",context)

def create_product(request):
	form = CreateProductForm()
	form2 = CreateCategoryForm()
	context = {
		'form':form,
		'form2':form2
	}
	return render(request,"product_create_form.html",context)

def create_category(request):

	if request.method == 'POST':
		form = CreateCategoryForm(request.POST)
		if form.is_valid():
			category = Category(
				category_name = form.cleaned_data['category_name'])
			category.save()
			return render(request, 'product_create_form.html', {'form': CreateProductForm()})
	else:  # 5
		# Create an empty form instance
		form = CreateCategoryForm()

	return render(request, 'category_create_form.html', {'form': form})
