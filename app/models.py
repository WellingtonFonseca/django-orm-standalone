# db/models.py
from django.db import models
from manager import init_django

init_django()


class Model(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# define models here
class User(models.Model):
    telephone = models.CharField(blank=False, default=None, max_length=100, null=True)  # noqa: E501
    age = models.CharField(blank=False, default=None, max_length=100, null=True)  # noqa: E501
