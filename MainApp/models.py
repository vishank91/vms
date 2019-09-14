from django.db import models
class Notice(models.Model):
    title=models.CharField(max_length=500)
    def __str__(self):
        return self.title
class MainSlider(models.Model):
    image=models.ImageField(upload_to='images',default=None)
    title=models.CharField(max_length=50,default='Sample',blank=True)
    def __str__(self):
        return self.title

class MainPics(models.Model):
    image=models.ImageField(upload_to='images',default=None)
    title=models.CharField(max_length=50,default='Sample',blank=True)
    def __str__(self):
        return self.title

class Topper(models.Model):
    name=models.CharField(max_length=30)
    image=models.ImageField(upload_to='images',default=None)
    className=models.CharField(max_length=20)
    marks=models.CharField(max_length=10)

    def __str__(self):
        return self.name+"\t"+self.className

class Birthday(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images', default=None)
    date=models.DateField()

    def __str__(self):
        return self.name

class News(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    image1=models.ImageField(upload_to='images',default=None,blank=True)
    image2 = models.ImageField(upload_to='images', default=None,blank=True)
    image3 = models.ImageField(upload_to='images', default=None,blank=True)
    image4 = models.ImageField(upload_to='images', default=None,blank=True)
    image5 = models.ImageField(upload_to='images', default=None,blank=True)

    def __str__(self):
        return self.title
