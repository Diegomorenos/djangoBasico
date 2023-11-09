from django.db import models

class Habitacion(models.Model):
    hab_numero = models.CharField(max_length = 3, primary_key = True)
    hab_estado = models.CharField(max_length = 7, null = True)
    tipo_hab_id = models.CharField(max_length = 7, null = True)
    hab_tarifa = models.CharField(max_length = 7, null = True)
    hab_capacidad = models.CharField(max_length = 7, null = True)


#python manage.py makemigrations
#python manage.py migrate