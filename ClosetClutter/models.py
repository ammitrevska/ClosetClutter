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


class Family(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    telephone = models.CharField(max_length=20)
    mail = models.EmailField(max_length=250)
    numOfMembers = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    numOfMembersMale = models.PositiveIntegerField()
    numOfMembersFemale = models.PositiveIntegerField()
    location = models.CharField(max_length=200)
    additionalInfo = models.TextField()
    NOTIFICATION_OPTIONS = (
        ('E', 'Email'),
        ('P', 'Phone'),
        ('B', 'Both')
    )
    notifyMe = models.CharField(max_length=1, choices=NOTIFICATION_OPTIONS)

    @property
    def is_family(self):
        return True

    def __str__(self):
        return self.name


class Individual(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    description = models.TextField()
    telephone = models.CharField(max_length=20)
    mail = models.EmailField(max_length=250)
    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDERS)
    SIZES = (
        ('XL', 'XL'),
        ('L', 'L'),
        ('M', 'M'),
        ('S', 'S'),
        ('XS', 'XS')
    )
    isIndividual = models.BooleanField(default=True)
    size = models.CharField(max_length=2, choices=SIZES)
    family = models.ForeignKey(Family, on_delete=models.CASCADE, blank=True, null=True)
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
        return self.firstName + self.lastName


class HumanitarianContainer(models.Model):
    city = models.CharField(max_length=20)
    address = models.CharField(max_length=30)
    picture = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.city + ", " + self.address


class Subscriber(models.Model):
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)


class Event(models.Model):
    TYPES = (('M', 'Meeting'),
             ('W', 'Workshop'))
    eventType = models.CharField(max_length=1, choices=TYPES)
    date = models.DateField()
    place = models.CharField(max_length=50)
    description = models.TextField()
    volunteersJob = models.TextField()
    picture = models.ImageField()

#


