from django.contrib import admin
from hotel_mgmt.models import Hotel,Room,RoomFacilities,Reservation

class HotelAdmin(admin.ModelAdmin):
	pass

class RoomAdmin(admin.ModelAdmin):
	pass

class RoomFacilitiesAdmin(admin.ModelAdmin):
	pass

class ReservationAdmin(admin.ModelAdmin):
	pass

admin.site.register(Hotel,HotelAdmin)
admin.site.register(Room,RoomAdmin)
admin.site.register(RoomFacilities,RoomFacilitiesAdmin)
admin.site.register(Reservation,ReservationAdmin)

