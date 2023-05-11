from django.contrib import admin
from book.models import Hotel, Client, Room, Employees, PivotTable

admin.site.register(Hotel)
admin.site.register(Client)
admin.site.register(Room)
admin.site.register(Employees)
admin.site.register(PivotTable)


# Register your models here.
