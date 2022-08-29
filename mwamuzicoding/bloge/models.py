from django.db import models

# Create your models here.
class Job(models.Model):
    picture = models.ImageField(upload_to ='images/')
    summary =models.CharField(max_length = 300)
    sex = models.CharField(max_length=100, default="gender")
    birth_date = models.DateField(blank=True, null=True)


    def __str__(self):
        return self.summary
    
    
