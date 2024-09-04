from django.db import models

# Create your models here.
class U_home(models.Model):
    s_name=models.CharField(max_length=30)
    s_description=models.CharField(max_length=50)
