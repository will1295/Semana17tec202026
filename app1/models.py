from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    stock = models.IntegerField()
    stock_min = models.IntegerField()

    def __str__(self):
        return "Nombre del producto: "+self.nombre+"Precio $"+str(self.precio)
