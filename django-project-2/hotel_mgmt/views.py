from django.shortcuts import render,redirect,get_object_or_404
from hotel_mgmt.models import Hotel,Room,RoomFacilities,Reservation
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse


def index(request):
	return render(request,'index_view.html',{})

class HotelListView(generic.ListView):
	model = Hotel
	template_name = 'hotel_list.html'
	paginate_by = 10

class HotelDetailView(generic.DetailView):
	model = Hotel
	template_name = 'hotel_detail.html'

class RoomFacList(generic.ListView):
	model = RoomFacilities
	template_name = 'facilities_list.html'
	paginate_by = 10

class RoomListView(generic.ListView):
	model = Room
	template_name = 'room_list.html'
	paginate_by = 10

class RoomDetailView(generic.DetailView):
	model = Room
	template_name = 'room_detail.html'

class ReservationListView(generic.ListView):
	model = Reservation
	template_name = 'reservation_list.html'
	paginate_by = 10

class ReservationDetailView(generic.DetailView):
	model = Reservation
	template_name = 'reservation_detail.html'
