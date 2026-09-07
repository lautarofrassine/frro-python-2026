from django.db import models

class Dueno(models.Model):
  nombre=models.CharField(max_length=100)
  dni=models.CharField(max_length=20,unique=True)
  email=models.EmailField()
  telefono=models.CharField(max_length=20)
  fecha_registro=models.DateTimeField(auto_now_add=True)
  obra_social=models.ForeignKey('ObraSocial',on_delete=models.SET_NULL,null=True,blank=True)
  

class ObraSocial(models.Model):
  nombre=models.CharField(max_length=100)
  porcentaje_cobertura=models.DecimalField(max_digits=5,decimal_places=2)
  tope_mensual=models.DecimalField(max_digits=10,decimal_places=2)
  servicio_cubierto=models.CharField(max_length=200)
