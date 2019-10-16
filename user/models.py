# from django.db import models
# from django.contrib.auth.models import AbstractUser
#
# from rest_framework.authtoken.models import Token
#
#
# class UserProfile(AbstractUser):
#     distance = models.CharField('Distance', max_length=255, blank=True)
#
#     def save(self, *args, **kwargs):
#         super(UserProfile, self).save(*args, **kwargs)
#         Token.objects.get_or_create(user=self)
#
#     class Meta:
#         verbose_name = "Usuário"
#         verbose_name_plural = "Usuários"
