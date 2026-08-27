from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Expense(models.Model):
    user=models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE,related_name='expense')
    title=models.CharField(max_length=20)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    date=models.DateField()