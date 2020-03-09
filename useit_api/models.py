from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    fix_id = models.IntegerField()
    def __str__(self):
            return '{0},{1},{2}'.format(self.name, self.description, self.fix_id)

class Comment(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    fix_id = models.IntegerField()
    def __str__(self):
           return '{0},{1},{2}'.format(self.name, self.description, self.fix_id)

class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    def __str__(self):
          return self.first_name


