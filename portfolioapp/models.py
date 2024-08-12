from django.db import models

class About(models.Model):
    short_description = models.TextField()
    description = models.TextField()
    image=models.ImageField(upload_to="about")

    class Meta:
        verbose_name = "About "
        verbose_name_plural = "About "

    def __str__(self):
        return "About"


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name



class RecentWork(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="works")

    def __str__(self):
        return self.title



class Client(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="clients", default="default.png")

    def __str__(self):
        return self.name
