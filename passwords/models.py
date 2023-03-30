from django.db import models
from users.models import User


class Password(models.Model):
    user = models.ForeignKey("users.User", related_name='credentials', null=False, blank=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default='')
    user_name = models.CharField(max_length=50, default='')
    pass_word = models.CharField(max_length=50, default='')
    description = models.TextField(default='')

    def __str__(self):
        return self.title
