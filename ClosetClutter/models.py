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
        ('XL', 'XL'),
        ('L', 'L'),
        ('M', 'M'),
        ('S', 'S'),
        ('XS', 'XS')
    )
    size = models.CharField(max_length=2, choices=SIZES)
    NOTIFICATION_OPTIONS = (
        ('E', 'Email'),
        ('P', 'Phone'),
        ('B', 'Both')
    )
    notifyMe = models.CharField(max_length=1, choices=NOTIFICATION_OPTIONS)

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
    numOfMembers = models.PositiveIntegerField(validators=[MinValueValidator(1)], verbose_name='Number of members')
    numOfMembersMale = models.PositiveIntegerField(verbose_name='Number of male members')
    numOfMembersFemale = models.PositiveIntegerField(verbose_name='Number of female members')
    location = models.CharField(max_length=200)
    additionalInfo = models.TextField()
    NOTIFICATION_OPTIONS = (
        ('E', 'Email'),
        ('P', 'Phone'),
        ('B', 'Both')
    )
    notifyMe = models.CharField(max_length=1, choices=NOTIFICATION_OPTIONS)
    members = models.ManyToManyField(Individual)

    @property
    def is_family(self):
        return True

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
    TYPES = (('M', 'Meeting'),
             ('W', 'Workshop'))
    eventType = models.CharField(max_length=1, choices=TYPES)
    date = models.DateField()
    place = models.CharField(max_length=50)
    description = models.TextField()
    volunteersJob = models.TextField()
    picture = models.ImageField(upload_to="event_images", null=True, blank=True)
