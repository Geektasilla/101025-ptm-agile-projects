from django.core.validators import MinLengthValidator
from django.db import models
from django.utils import timezone
from projects.enums import STATUSES_CHOICES, PRIORITY_CHOICES


class Task(models.Model):
    name = models.CharField(max_length=50, validators=[MinLengthValidator(10)],unique=True)
    description = models.TextField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=15, choices=STATUSES_CHOICES)
    priority = models.CharField(max_length=15, choices=PRIORITY_CHOICES)
    project = models.ForeignKey(
        'Project',
        on_delete=models.PROTECT,
        related_name='tasks'
    )
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(default=timezone.now())
    deleted = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name