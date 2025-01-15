from django.db import models

class Termit(models.Model):
    termi = models.CharField(max_length = 20, default = "termi")
    term = models.CharField(max_length = 20, default = "term")
    selitys = models.CharField(max_length = 20000, default = "selitys")
    def __str__(self):
        return f"{self.termi} "
# Create your models here.
