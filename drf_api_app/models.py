from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class Things(models.Model):
    title=models.CharField(max_length=64)
    purchaser=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    description=models.TextField(max_length=64,default='')

    def __str__(self):
            return self.title