from django.contrib import admin

from airlines.models import Crew, Plane, Order, Client

admin.site.register(Crew)
admin.site.register(Plane)
admin.site.register(Order)
admin.site.register(Client)
