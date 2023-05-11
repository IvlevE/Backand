from rest_framework.serializers import ModelSerializer

from book.models import Hotel, Client, Room, Employees, PivotTable


class HotelSerializer(ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('id','Name_Hotel','Address_Hotel')

class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ('id','user_id','Last_Name','First_Name','Mid_Name','Tel')

class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = ('id','Hotel','Name_Room', 'Type_Room','Capacity','Type_Room')

class EmployeesSerializer(ModelSerializer):
    class Meta:
        model = Employees
        fields = ('id','Hotel','Last_Name','First_Name','Mid_Name','Tel','Post','POR')

class PivotTableSerializer(ModelSerializer):
    class Meta:
        model = PivotTable
        fields = ('id','Hotel','Room','Client','DepartureDate','ArrivalDate','Final_price')