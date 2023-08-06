from django.db import models
import uuid
# Create your models here.

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Video(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    #
    print(uuid)
    # print(uuid.uuid4)
    url = models.URLField()
    # type = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    vname = models.CharField(max_length=255)
    resolution = models.CharField(max_length=20)

