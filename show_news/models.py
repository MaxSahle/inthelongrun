from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.utils.encoding import python_2_unicode_compatible
from django.db import models

@python_2_unicode_compatible
class News(models.Model):
    url = models.CharField(max_length=500)
    headline = models.CharField(max_length=150)
    date = models.DateField()
    received = models.DateTimeField()
    category = models.CharField(max_length = 100)
    source = models.CharField(max_length = 100)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.headline
	
    class Meta:
        unique_together = (("url", "headline"),)

@python_2_unicode_compatible
class Sources(models.Model):
    name = models.CharField(max_length = 150)
    url = models.CharField(max_length = 500)
    rangking = models.IntegerField()
    code = models.CharField(max_length = 2000)
    print_code = models.CharField(max_length = 2000)
    def print_code(self):
	return self.code.replace(" stopline ","\n") <= self.print_code
    def __str__(self):
        return self.name