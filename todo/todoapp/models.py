from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=50)
    owner = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    content = models.CharField(max_length=300)
    complete = models.BooleanField(default=False)
    enddate = models.DateField()
    