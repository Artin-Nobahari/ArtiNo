from django.db import models
from apps.core.models import BaseModel, SlugModel


# Create your models here.
class Department(SlugModel):
    """"""

    name = models.CharField(max_length=50)


class Ticket(BaseModel):
    """"""

    PRIORITY = [
        ("normal", "normal"),
        ("medium", "medium"),
        ("urgent", "urgent"),
    ]

    subject = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    priority = models.CharField(choices=PRIORITY)
    text = models.TextField()

    def __str__(self):
        return self.subject