from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=50,unique=True)
    description = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

