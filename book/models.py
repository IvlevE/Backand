from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models import DO_NOTHING


class Hotel(models.Model):
    Name_Hotel = models.CharField(verbose_name='name hotel', max_length=150)
    Address_Hotel = models.CharField(verbose_name='address hotel', max_length=300)

    def __str__(self):
        return f'{self.Name_Hotel} {self.Address_Hotel}'

    class Meta:
        verbose_name='Отель'
        verbose_name_plural='Отели'

class Room(models.Model):
    Hotel = models.ForeignKey(Hotel, verbose_name='hotel', on_delete=models.CASCADE)
    Name_Room = models.CharField(verbose_name='name room', max_length=150)
    Capacity = models.IntegerField(verbose_name='capacity', max_length=2)
    Type_Room = models.CharField(verbose_name='type room', max_length=50)
    Price = models.IntegerField(verbose_name='price', max_length=6)

    def __str__(self):
        return f'{self.Name_Room} {self.Type_Room} {self.Capacity}'

    class Meta:
        verbose_name='Номер'
        verbose_name_plural='Номера'

class Employees(models.Model):
    Hotel = models.ForeignKey(Hotel, verbose_name='hotel', on_delete=models.CASCADE)
    Last_Name = models.CharField(verbose_name='last name', max_length=20)
    First_Name = models.CharField(verbose_name='first name', max_length=20)
    Mid_Name = models.CharField(verbose_name='mid name', max_length=20, blank=True)
    Post = models.CharField(verbose_name='post', max_length=20)
    POR = models.CharField(verbose_name='places of residence', max_length=300)
    Tel = models.CharField(verbose_name='telephone', max_length=20)

    def __str__(self):
        return f'{self.Last_Name} {self.First_Name} {self.Mid_Name}'

    class Meta:
        verbose_name='Сотрудник'
        verbose_name_plural='Сотрудники'

class Client(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    Last_Name = models.CharField(verbose_name='last name', max_length=20)
    First_Name = models.CharField(verbose_name='first name', max_length=20)
    Mid_Name = models.CharField(verbose_name='mid name', max_length=20, blank=True)
    Tel = models.CharField(verbose_name='telephone', max_length=20)

    def __str__(self):
        return f'{self.Last_Name} {self.First_Name} {self.Mid_Name}'

    class Meta:
        verbose_name='Клиент'
        verbose_name_plural='Клиенты'

class PivotTable(models.Model):
    Hotel = models.ManyToManyField(Hotel, verbose_name='Hotel')
    Room = models.ManyToManyField(Room, verbose_name='Room')
    Client = models.ManyToManyField(Client, verbose_name='Client')
    DepartureDate = models.DateField(verbose_name='relize', default=datetime.date.today())
    ArrivalDate = models.DateField(verbose_name='relize', default=None)
    Final_price = models.IntegerField(verbose_name='final')

    def __str__(self):
        return f'{self.Client} {self.Hotel} {self.Room} {self.ArrivalDate} {self.DepartureDate}'

    class Meta:
        verbose_name='Бронь'
        verbose_name_plural='Брони'







