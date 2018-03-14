from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 100)  # blog title
    category = models.CharField(max_length = 50, blank = True) # blog tag
    date_time = models.DateTimeField(auto_now_add = True) #blog time
    content = models.TextField(blank = True, null = True) # blog article

    #getURL and transmit the format of url
    def get_absolute_url(self):
        path = reverse('detail', kwargs={'id':self.id})
        return "http://127.0.0.1:8000%s" % path
    #python2 use__unicode__, pythons use __str__
    def __str__(self):
        return self.title

    class Meta: # descend order by time
        ordering = ['-date_time']