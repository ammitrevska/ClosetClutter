from django.contrib.admin import forms
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class CharityOrg(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    telephone = models.CharField(max_length=20)
    mail = models.EmailField(max_length=250)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Individual(models.Model):
    firstName = models.CharField(max_length=50, verbose_name='First name')
    lastName = models.CharField(max_length=50, verbose_name='Second name')
    description = models.TextField()
    telephone = models.CharField(max_length=20)
    mail = models.EmailField(max_length=250)
    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDERS, default='M')

    SIZES = (
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
    )
    size = models.CharField(max_length=4, choices=SIZES)
    NOTIFICATION_OPTIONS = (
        ('E', 'Email'),
        ('P', 'Phone'),
        ('B', 'Both')
    )
    notifyMe = models.CharField(max_length=1, choices=NOTIFICATION_OPTIONS, verbose_name="Notify me")
    location = models.CharField(max_length=200, null=True, blank=True)
    additionalInfo = models.TextField(verbose_name="Additional information", null=True, blank=True)

    @property
    def is_family(self):
        return False

    def __str__(self):
        return self.firstName + " " + self.lastName


class Family(models.Model):
    name = models.CharField(max_length=50, verbose_name="Surname")
    description = models.TextField()
    telephone = models.CharField(max_length=20)
    mail = models.EmailField(max_length=250)
    location = models.CharField(max_length=200)
    additionalInfo = models.TextField(verbose_name="Additional information",null=True, blank=True)
    NOTIFICATION_OPTIONS = (
        ('E', 'Email'),
        ('P', 'Phone'),
        ('B', 'Both')
    )
    notifyMe = models.CharField(max_length=1, choices=NOTIFICATION_OPTIONS, null=True, blank=True)
    members = models.ManyToManyField(Individual)

    @property
    def is_family(self):
        return True

    # @property
    # def num_small_members(self):
    #     return self.members.filter(size='M').count()

    def count_members_m_m(self):
        filtered_members = self.members.filter(gender='M', size='M')
        return filtered_members.count()

    def count_members_m_s(self):
        filtered_members = self.members.filter(gender='M', size='S')
        return filtered_members.count()

    def count_members_m_l(self):
        filtered_members = self.members.filter(gender='M', size='L')
        return filtered_members.count()

    def count_members_m_l(self):
        filtered_members = self.members.filter(gender='M', size='XL')
        return filtered_members.count()

    def count_members_m_l(self):
        filtered_members = self.members.filter(gender='M', size='XXL')
        return filtered_members.count()

    def count_members_f_s(self):
        filtered_members = self.members.filter(gender='F', size='S')
        return filtered_members.count()

    def count_members_f_m(self):
        filtered_members = self.members.filter(gender='F', size='M')
        return filtered_members.count()

    def count_members_f_l(self):
        filtered_members = self.members.filter(gender='F', size='L')
        return filtered_members.count()

    def count_members_f_l(self):
        filtered_members = self.members.filter(gender='F', size='XL')
        return filtered_members.count()

    def count_members_f_l(self):
        filtered_members = self.members.filter(gender='F', size='XXL')
        return filtered_members.count()

    def __str__(self):
        return self.name


class HumanitarianContainer(models.Model):
    city = models.CharField(max_length=20)
    address = models.CharField(max_length=30)
    picture = models.ImageField(upload_to="humanitarianContainers_images", null=True, blank=True)

    def __str__(self):
        return self.city + ", " + self.address


class Subscriber(models.Model):
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=10)


class Event(models.Model):
    TYPES = (('Meeting', 'Meeting'),
             ('Workshop', 'Workshop'))
    eventType = models.CharField(max_length=10, choices=TYPES)
    date = models.DateField()
    place = models.CharField(max_length=50)
    description = models.TextField()
    volunteersJob = models.TextField()
    picture = models.ImageField(upload_to="event_images", null=True, blank=True)
