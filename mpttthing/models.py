from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class File(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='child')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name
