from django.db import models
from django.core.urlresolvers import reverse
from restaurantesapp.models import RestaurantModel

class Platillo(models.Model):

    nombre = models.CharField(max_length=255)
    restaurante = models.ForeignKey(RestaurantModel, related_name='platillos')


    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('platillos:detail', kwargs={'pk':self.pk})

    def get_absolute_url_edit(self):
        return reverse('platillos:edit', kwargs={'pk': self.pk})

    def get_absolute_url_delete(self):
        return reverse('platillos:delete', kwargs={'pk': self.pk})
