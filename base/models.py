import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class BaseModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __repr__(self):
        sensitive_fields = {"password", "secret", "ssn", "token", "auth_token"}
        attrs = []
        for field in self._meta.fields:
            if field.name in sensitive_fields:
                attrs.append(f"{field.name}=<redacted>")
            else:
                attrs.append(f"{field.name}={repr(getattr(self, field.name))}")

        return f"{self.__class__.__name__}({', '.join(attrs)})"


class User(BaseModel, AbstractUser):
    pass


class Department(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Employee(BaseModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
