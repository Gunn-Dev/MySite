from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    signature = models.CharField(max_length=140, default='Your Name or Favorite Quote')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
