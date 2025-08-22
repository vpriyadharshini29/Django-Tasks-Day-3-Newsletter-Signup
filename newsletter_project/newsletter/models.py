from django.db import models

class Subscriber(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # unique ensures no duplicates

    def __str__(self):
        return f"{self.name} ({self.email})"
