from django.db import models

# Create your models here.

class Propietario(models.Model):
    opciones_nacionalidad = (
        ('ecuatoriana','Ecuatoriana'),
        ('peruana','Peruana'),
        ('colombiana','Colombiana'),
        )

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField("edad del propietario")
    nacionalidad = models.CharField(max_length=30, \
        choices=opciones_nacionalidad)

    def __str__(self):
        return "%s %s %d %s" % (self.nombre,
                self.apellido,
                self.edad,
                self.nacionalidad)

class Departamento(models.Model):
    costoDepartamento = models.IntegerField("costo departamento")
    numCuartos = models.IntegerField("numero de cuartos")
    numBanios = models.IntegerField("numero de baños")
    valorAlicuota = models.IntegerField("valor alicuota")

    Propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE,
            related_name="departamentos")

    def __str__(self):
        return "%d %d %d %d" % (self.costoDepartamento,
         self.numCuartos,
         self.numBanios,
         self.valorAlicuota)
