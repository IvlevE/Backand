from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from book.permissions import IsStaff, IsStaffOrReadOnly
from rest_framework.viewsets import ModelViewSet
from book.models import Hotel, Client, Room, Employees, PivotTable
from book.seriallizator import HotelSerializer, ClientSerializer, RoomSerializer, EmployeesSerializer, PivotTableSerializer

class HotelViewSet(ModelViewSet):
    permission_classes = (IsStaffOrReadOnly, )
    serializer_class = HotelSerializer
    queryset = Hotel.objects.all()

class ClientViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

    def get_my_info(self):
        user = self.request.user
        return Client.objects.filter(user = user)

class RoomViewSet(ModelViewSet):
    permission_classes = (IsStaffOrReadOnly,)
    serializer_class = RoomSerializer
    queryset = Room.objects.all()

class EmployeesViewSet(ModelViewSet):
    permission_classes = (IsStaff,)
    serializer_class = EmployeesSerializer
    queryset = Employees.objects.all()

    #Выбирает первых 3 сотрудников (по фамилии)
    @action(methods=['get'], detail=False, url_path='last-3')
    def get_last_3(self,request):
        set_emp = self.queryset.order_by('Last_Name')[:3]
        data = self.serializer_class(set_emp, many=True).data
        return Response(data)

    @action(methods=['get'], detail=False, url_path='Accountant')
    def get_only_accountant(self,request):
        role = request.query_params.get('Post')
        set_acc = self.get_queryset().filter(Post = role)
        data = self.serializer_class(set_acc, many=True).data
        return Response(data)

class PivotTableViewSet(ModelViewSet):
    permission_classes = (IsStaff,)
    serializer_class = PivotTableSerializer
    queryset = PivotTable.objects.all()

    #Выбирает последнюю бронь
    @action(methods=['get'], detail=False, url_path='PT-last')
    def PT_get_last(self, request):
        set_emp = self.queryset.order_by('DepartureDate')[:1]
        data = self.serializer_class(set_emp, many=True).data
        return Response(data)
