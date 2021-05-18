from django.db import models

from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
#
from .managers import UserManager

class dependencia(models.Model):
    dependencia = models.CharField(max_length=30)

    def __str__(self):
        return self.dependencia

class User(AbstractBaseUser, PermissionsMixin):


    AR_CHOICES = (
        ('ADMIN', 'Administracion'),
        ('COMER', 'Comercial'),
        ('GH', 'Gestion_humana'),
        ('OPER', 'Operaciones'),
        ('ORG_M', 'Organización y metodos'),
        ('SE_NA', 'Seguridad_nacional'),
        ('SER_CL', 'servicio_al_cliente'),
        ('SIG', 'Sig'),
        ('TECNO', 'Tecnologia'),
    )
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otros'),
    )


    username = models.CharField(max_length=10, unique=True)
    email = models.EmailField()
    nombres = models.CharField(max_length=30, blank=True)
    apellidos = models.CharField(max_length=30, blank=True)
    genero = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    Area = models.CharField(max_length=6, choices=AR_CHOICES, blank=True)
    dependencia = models.ManyToManyField(dependencia)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email',]   

    objects = UserManager()

    def get_short_name(self):
        return self.username
    
    def get_full_name (self):
        return self.nombres + ' ' + self.Area


