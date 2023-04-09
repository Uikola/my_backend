from django.db import models
from core.models import BaseModel


class File(BaseModel):
    title = models.CharField(max_length=128, default='No title')
    file = models.FileField(upload_to='files')

    def __str__(self):
        return self.title
