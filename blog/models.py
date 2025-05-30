from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=256, blank=False)
    #slug = models.SlugField(max_length=256)
    content = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    udpated_at = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.title
    