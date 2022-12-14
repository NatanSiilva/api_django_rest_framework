from django.db import models

from simple_history.models import HistoricalRecords


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.BooleanField("Status", default=True)
    created_at = models.DateTimeField("Created At", auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField("Updated At", auto_now=True, auto_now_add=False)
    deleted_date = models.DateTimeField("Deleted", auto_now=True, auto_now_add=False)

    historical = HistoricalRecords(user_model="users.User", inherit=True)

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        abstract = True
        verbose_name = "BaseModel"
        verbose_name_plural = "BaseModels"
