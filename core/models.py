from django.db import models

class ServerPackage(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    cpu_cores = models.PositiveIntegerField()
    ram_gb = models.PositiveIntegerField()
    storage_gb = models.PositiveIntegerField()
    price_per_month = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name