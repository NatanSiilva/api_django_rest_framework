from django.db import models


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.BooleanField("Status", default=True)
    created_at = models.DateTimeField("Created At", auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField("Updated At", auto_now=True, auto_now_add=False)
    deleted_date = models.DateTimeField("Deleted", auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True
        verbose_name = "BaseModel"
        verbose_name_plural = "BaseModels"
