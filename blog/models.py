
from django.db import models
from django.utils import timezone

"""
  ### Class Post
  ### date : 05/05/2017
  ### Author: Carlos Xavier 
  ### está classe tem por finalidade automatizar a publicação de post.


"""
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
