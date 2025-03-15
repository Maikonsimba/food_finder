from django.db import models

class Driver(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, unique=True)
    vehicle_type = models.CharField(max_length=50, choices=[('bodaboda', 'Bodaboda'), ('bajaji', 'Bajaji'), ('taxi', 'Taxi')])
    license_number = models.CharField(max_length=50, unique=True)
    location = models.CharField(max_length=255)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.vehicle_type}"
