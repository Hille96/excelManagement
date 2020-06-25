from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField


class ExcelData(models.Model):
    """Model definition for ExcelData."""
    title = models.CharField(max_length=50, blank=True, null=True)
    data = JSONField()

    class Meta:
        """Meta definition for ExcelData."""

        verbose_name = 'ExcelData'
        verbose_name_plural = 'ExcelData'


class CustomViewFilter(models.Model):
    """Model definition for CustomViewFilter."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    columns = JSONField()

    class Meta:
        """Meta definition for CustomViewFilter."""

        verbose_name = 'CustomViewFilter'
        verbose_name_plural = 'CustomViewFilters'