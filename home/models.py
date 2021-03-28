from django.db import models

# Create your models here.
CATEGORY = (('vector','vector'),('raster','raster'),('ui','ui'),('printing','printing'),('','default'))
STATUS = (('active','active'),('','default'))
class Contact(models.Model):
    name = models.CharField(max_length=300)
    email=models.CharField(max_length=300)
    subject = models.TextField()
    message=models.TextField()

    def __str__(self):
        return self.name,self.email,self.subject

class Review(models.Model):
    name = models.CharField(max_length=250)
    post = models.CharField(max_length=200, blank=True,null=True)
    image = models.TextField(blank=True)
    comment = models.TextField()

    def __str__(self):
        return self.name,self.post



class Project(models.Model):
    image=models.TextField()
    title=models.CharField(max_length=200)
    type=models.CharField(max_length=200)
    category = models.CharField(choices=CATEGORY,blank=True,max_length=100)
    status = models.CharField(choices= STATUS, blank=True, max_length=100)

    def __str__(self):
        return self.title,self.type

class Skills(models.Model):
    name = models.CharField(max_length=300)
    level = models.IntegerField()

    def __str__(self):
        return self.name