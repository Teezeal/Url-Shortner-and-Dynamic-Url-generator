from django.db import models

class Urls(models.Model):
    original_url = models.URLField(max_length=2048)
    short_url = models.CharField(max_length=8, unique=True)
   

    def __str__(self) -> str:
        return self.short_url
    

