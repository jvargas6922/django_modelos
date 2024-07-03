from django.db import models

# Create your models here.
class Persona(models.Model):
    name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField()
    age = models.IntegerField()
    
    def __str__(self):
        return f'{self.name} {self.last_name}, {self.age} años y Email: {self.email}'
        # joffred vargas, 38 años y Email:vargaszambranoj@gmail.com