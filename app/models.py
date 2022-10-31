# db/models.py
from django.db import models


class Model(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# define models here


class User(models.Model):
    telephone = models.CharField(blank=False, max_length=100, null=False)
