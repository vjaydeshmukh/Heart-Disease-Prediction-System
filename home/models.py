from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(null=True)
    detail = models.TextField(default='')
    image = models.FileField(upload_to='articles')
    date = models.DateField(auto_now_add=True)

    class Meta():
        ordering = ['-date']

    def __str__(self):
        return self.title


class Hospital(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=True)
    location = models.CharField(max_length=100)
    details = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20)
    phone_number2 = models.CharField(max_length=20, blank=True)
    phone_number3 = models.CharField(max_length=20, blank=True)
    image = models.ImageField(upload_to='hospitals', blank=True)

    def __str__(self):
        return self.name



class Doctor(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=True)
    qualification = models.CharField(max_length=150, blank=True)
    details = models.TextField(blank=True)
    hospital = models.ForeignKey(Hospital, on_delete=models.PROTECT, null=True, blank=True)
    schedule = models.TextField(blank=True)
    image = models.ImageField(upload_to='doctors', blank=True)

    def __str__(self):
        return self.name


class Register(models.Model):
    username = models.CharField(max_length=20)
    email_address = models.EmailField()
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=6)

    def __str__(self):
        return self.username