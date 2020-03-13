from django.shortcuts import render,redirect,get_object_or_404
from hotel_mgmt.models import Hotel,Room,RoomFacilities,Reservation,RoomType
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse
from hotel_mgmt.forms import ReservationForm


def index(request):
	return render(request,'index_view.html',{})

class RoomTypeView(generic.ListView):
	model = RoomType
	template_name = 'room_type_list.html'
	paginate_by = 10

class RoomTypeCreateView(CreateView):
	model = RoomType
	fields = '__all__'
	# sucess_url = reverse('')

class RoomTypeDetailView(generic.DetailView):
	model = RoomType
	template_name = 'room_type_detail.html'

class RoomFacList(generic.ListView):
	model = RoomFacilities
	template_name = 'facilities_list.html'
	paginate_by = 10

class RoomCreateView(CreateView):
	model = Room
	fields = '__all__'

	def get_success_url(self):
		return reverse('room-list')

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

def getRooms(request,pk):
	room_type = RoomType.objects.get(pk=pk)
	rooms = room_type.room_set.all()
	return render(request,'room_detail.html',{'room_list':rooms})

def doReservation(request):
	if request.method == 'POST':
		form = ReservationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect(reverse('reservation-list'))
	else:
		form = ReservationForm()
		return render(request,'reservation.html',{'form':form})

	
