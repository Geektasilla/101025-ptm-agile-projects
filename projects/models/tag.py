from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)
    deadline_date = models.DateTimeField()

    tags = models.ManyToManyField(
        'Tag',
        related_name='tasks'
    )

    def __str__(self):
        return self.name


