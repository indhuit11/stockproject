from django.contrib import admin
from django.db import models

class Student (models.Model):
   stdid=models.IntegerField(primary_key=True)
   stdname=models.CharField(max_length=30)
   mychoice=[('java','java'),('python','python'),('php','php')]
   course=models.CharField(choices=mychoice,max_length=20)

   def __str__(self):
         return f'{self.stdid}-{self.stdname}-{self.course}'


class Book(models.Model):
   bookid=models.IntegerField(primary_key=True)
   mybook=[('c','c'),('c++','c++'),('python','python')]
   bookname = models.CharField(choices=mybook,max_length=30)
   myauthor = [('dennis ritchie','dennis ritchie'),('bjourne stratustrup','bjourne stratustrup'),('guido van rosuum','guido van rosuum')]
   author=models.CharField(choices=myauthor,max_length=20)
   bookcount=models.IntegerField()
   recvdate=models.DateField()

   def __str__(self):
         return f'{self.bookid}-{self.bookname}-{self.author}'

class Issued(models.Model):
   issid = models.IntegerField(primary_key=True)
   issdate=models.DateField()
   bookid=models.ForeignKey(Book,on_delete=models.CASCADE)
   student=models.ForeignKey(Student,on_delete=models.CASCADE)
   bookcount=models.IntegerField()

   def __str__(self):
      return f'{self.issid}-{self.issdate}-{self.bookid}-{self.student}-{self.bookcount}'


class IssuedAdmin(admin.ModelAdmin):
   list_display = ('__str__','issid','issdate')


