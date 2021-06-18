from django.db import models

# Create your models here.
class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    content = models.TextField()
    author = models.CharField(max_length=30)
    urlToImage = models.CharField(max_length=1000)
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title + ' by ' + self.author
