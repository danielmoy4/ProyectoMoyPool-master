from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Registro_Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # Otros campos según tu modelo

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    @classmethod
    def buscar_por_email(cls, email):
        return cls.objects.filter(email=email).first()

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=255)
    cantidad = models.IntegerField()
