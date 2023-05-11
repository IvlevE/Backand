from django.urls import path, include
from rest_framework.routers import DefaultRouter

from  book.views import RoomViewSet, HotelViewSet, ClientViewSet, EmployeesViewSet, PivotTableViewSet

router = DefaultRouter()
router.register('hotels', HotelViewSet)
router.register('rooms', RoomViewSet)
router.register('clients', ClientViewSet)
router.register('Employees', EmployeesViewSet)
router.register('PivotTables', PivotTableViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls))

]