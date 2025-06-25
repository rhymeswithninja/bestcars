from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator

class CarMake(models.Model):
    name = models.CharField(max_length=100, help_text="Enter car make name")
    description = models.TextField(help_text="Enter car make description", blank=True)

    def __str__(self):
        return self.name

class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name='car_models')
    name = models.CharField(max_length=100, help_text="Enter car model name")
    type = models.CharField(
        max_length=20,
        choices=[
            ('SEDAN', 'Sedan'),
            ('SUV', 'SUV'),
            ('WAGON', 'Wagon'),
            ('COUPE', 'Coupe'),
            ('CONVERTIBLE', 'Convertible'),
            ('HATCHBACK', 'Hatchback')
        ],
        help_text="Select car model type"
    )
    year = models.IntegerField(
        validators=[
            MinValueValidator(2015),
            MaxValueValidator(2023)
        ],
        help_text="Enter car model year"
    )
    def __str__(self):
        return f"{self.name} ({self.year}) - {self.car_make.name}"