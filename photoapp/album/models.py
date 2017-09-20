from django.db import models


# Create your models here.


class Photo(models.Model):
    description = models.CharField(max_length=200)
    image = models.ImageField(null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-timestamp"]