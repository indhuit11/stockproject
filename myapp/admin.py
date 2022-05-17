from django.contrib import admin
from .models import Student,Book,Issued

admin.site.register(Student)
admin.site.register(Book)
admin.site.register(Issued)