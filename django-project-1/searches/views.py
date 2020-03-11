from django.shortcuts import render
from . models import SearchQuery
from visitor_app.models import  *


def search_view(request):
	query = request.GET.get('q',None)
	user = None
	if request.user.is_authenticated:
		user = request.user
	context = {"query":query}
	if query is not None:
		SearchQuery.objects.create(user=user,query=query)
		visit_list = Visit.objects.all().search(query=query)
		context['visit_list'] = visit_list
	return render(request,'view.html',context)
