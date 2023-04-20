from django.db import models
from users.models import User
from encrypted_model_fields.fields import EncryptedCharField


class Password(models.Model):
    user = models.ForeignKey("users.User", related_name='credentials', null=False, blank=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default='')
    user_name = EncryptedCharField(max_length=50)
    pass_word = EncryptedCharField(max_length=50)
    description = models.TextField(default='')

    def __str__(self):
        return self.title
