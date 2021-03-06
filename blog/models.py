from datetime import datetime
import time
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible  # only if you need to support Python 2
class Post(models.Model):
    title = models.CharField(max_length=50)
    created_on = models.DateTimeField(default=datetime.now, blank=True)
    body = models.TextField()
    tags = models.CharField(max_length=200, default='', blank=True)
    image = models.CharField(max_length=100, null=True, blank=True)
    published = models.BooleanField()

    def __str__(self):
        return self.title

    def serialize(self):

        serialized_tags = []
        for tag in self.tags.split(','):
            serialized_tags.append(tag.strip())

        serialized_comments = []
        for comment in self.comments.all():
            serialized_comments.append(comment.serialize())

        return {
            'id': self.pk,
            'title': self.title,
            'createdOn': int(time.mktime(self.created_on.timetuple())*1000),
            'body': self.body,
            'comments': serialized_comments,
            'tags': serialized_tags,
            'image': self.image
        }


@python_2_unicode_compatible
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField()
    author = models.CharField(max_length=100)
    created_on = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.post.title + ' - ' + self.author + ' - ' + self.created_on.strftime('%d/%m/%Y')

    def serialize(self):
        return {
            'author': self.author,
            'createdOn': int(time.mktime(self.created_on.timetuple())*1000),
            'body': self.body
        }


@python_2_unicode_compatible
class Repo(models.Model):
    name = models.CharField(max_length=50)
    logbook_url = models.CharField(max_length=100)
    last_scraped = models.DateTimeField(default=datetime.now)
    enabled = models.BooleanField()

    def __str__(self):
        return self.name + ' - ' + self.logbook_url
