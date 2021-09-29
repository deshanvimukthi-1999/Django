from django.db import models
from django.contrib.auth.models import AbstractUser

import uuid

from apps.common.models import Company


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254, blank=True)
    contact_no = models.CharField(max_length=12)
    company = models.ForeignKey(Company, related_name='users', on_delete=models.CASCADE)

