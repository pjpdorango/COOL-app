from django.db.models import *
from django.db import models

# from ..Subject.models import 

# Create your models here.
class Collection(Model):
    name: CharField = CharField(
        max_length=25,
        blank=False,
        null=False
    )

    visibility: models.DateField