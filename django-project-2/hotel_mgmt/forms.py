from django import forms
from hotel_mgmt.models import *
from django.contrib.admin.widgets import FilteredSelectMultiple


class ReservationForm(forms.ModelForm):
	room_id = forms.ModelMultipleChoiceField(
        queryset=Room.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
	class Meta:
		model=Reservation
		fields = ('customer_name','customer_address','customer_contact','customer_email','room_type','room_id','days','total_price')