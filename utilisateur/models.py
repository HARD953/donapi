from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
# Create your models here.

class DonateurUser(AbstractBaseUser,PermissionsMixin):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField(max_length=255,unique=True)
    numero=models.CharField(max_length=30)
    organisations=models.CharField(max_length=30,default="null")
    # adresse=models.CharField(max_length=300, blank=True, null=True)
    # about_me=models.TextField(max_length=500, blank=True, null=True)
    # create=models.DateTimeField(auto_now_add=True)
    # profile_image=models.ImageField(null=True)
    # is_active=models.BooleanField(default=False)
    # is_staff=models.BooleanField(default=False)
    # is_superuser=models.BooleanField(default=False)
    # is_user=models.BooleanField(default=False)
    # is_agent=models.BooleanField(default=False)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','password']
    
    def __str__(self):
        return self.first_name

class EffectuerDon(models.Model):
    donateur=models.ForeignKey(DonateurUser,on_delete=models.CASCADE)
    cible=models.CharField(max_length=100,default='null')
    categorie=models.CharField(max_length=100,default='null')
    nature=models.CharField(max_length=100,default='null')
    lieu_reception=models.CharField(max_length=100,default='null')
    photo=models.CharField(max_length=100,default='null')
    Etat=models.CharField(max_length=100,default='null')
    create=models.DateTimeField(auto_now_add=True)
    montant=models.FloatField(max_length=100,default='null')
    provider=models.CharField(max_length=100,default='null')
