from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=80, unique=True)
    email = models.EmailField(max_length=80, unique=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    favoArtist = models.CharField(max_length=80)
    geneFavo = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'api_view_users'
