from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100)
    # blog = models.ManyToManyField(Blog, related_name='tags')

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    tags = models.ManyToManyField(Tag, related_name='tags')

    def __str__(self):
        return self.title
    


