from django.db import models

class Task(models.Model):
    title = models.TextField()
    description = models.TextField()
    completed = models.BooleanField(default=False)
    category = models.ForeignKey(to='Category', to_field='name', on_delete=models.CASCADE)

class Category(models.Model):
    name = models.TextField();
    