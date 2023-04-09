from core.models import BaseModel
from django.db import models


class Video(BaseModel):
    title = models.CharField(max_length=128, default='NoneTitle')
    url = models.URLField(max_length=512)
