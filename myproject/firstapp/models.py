from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Login_info(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField()

    class Meta:
        db_table = 'UserInfo'
        verbose_name = _('login_Information')
        verbose_name_plural = _('login_Informations')
        ordering = ('username',)
    def __str__(self):
        return self.username
