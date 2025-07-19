from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class DiseaseRecord(models.Model):
    
    DISEASE_CHOICES = [
        ('DR','Diabetic Retinopathy'),
        ('PN','Pneumonia'),
        ('LC','Lung Cancer'),
    ]
    
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    disease = models.CharField(max_length=3,choices=DISEASE_CHOICES)
    image=models.ImageField(upload_to='uploads/')
    result=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.get_disease_display()} - {self.result}"