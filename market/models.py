from django.db import models
from django.contrib.auth.models import User

TYPE = (
    ('Гіпермаркет', 'Гіпермаркет'),
    ('Супермаркет', 'Супермаркет'),
    ('Маркет', 'Маркет')
)


class Profile(models.Model):
    administrator = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    market = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=50, null=True)
    type = models.CharField(max_length=20, choices=TYPE, null=True)

    def __str__(self):
        return f'{self.market} - {self.administrator.username}'