from django.db import models
from django.contrib.auth.models import User
from base.models import BaseModel
# Create your models here.

class profile(BaseModel):
    user=models.OneToOneField(User,on_delete=models.CASCADE, related_name='profile')
    is_email_verifide=models.BooleanField(default=False)
    emai_token=models.CharField(max_length=100,null=True,blank=True)
    profile_image=models.ImageField(upload_to='profile')