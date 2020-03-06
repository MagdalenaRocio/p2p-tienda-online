from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nomCat = models.CharField(max_length=70)

    def __str__(self):
        return self.nomCat

class Producto(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=20,null=True)
    precio = models.IntegerField(null=True)
    descripcion = models.CharField(max_length=250,null=True)
    producto_fields = models.ImageField(upload_to='static/img')
    fkCategoria = models.ForeignKey(Categoria, on_delete = models.CASCADE, null= True)

    def __str__(self):
        return self.nombre

class Carrito(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=20,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    estado = models.BooleanField(default=True, verbose_name='Estado')

    class Meta:
        verbose_name = 'Carrito'
        
    def __str__(self):
        return f'{self.cantidad} of {self.producto}'

