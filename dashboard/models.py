from django.db import models
from django.contrib.auth.models import User
from market.models import Profile

CATEGORY = (
    ('Крупі і макарони', 'Крупі і макарони'),
    ('Овочі та фрукти', 'Овочі та фрукти'),
    ('Мучне', 'Мучне'),
    ('М`ясо та яйця', 'М`ясо та яйця'),
    ('Алкогольні напої', 'Алкогольні напої'),
    ('Солодощі', 'Солодощі'),
    ('Риба та морепродукти', 'Риба та морепродукти'),
    ('Краса та здоров`я', 'Краса та здоров`я'),
    ('Господарські товари', 'Господарські товари'),
    ('Будинок і сад', 'Дім і сад'),
    ('Молочні продукти', 'Молочні продукти'),
    ('Напої', 'Напої'),
    ('Заморожене', 'Заморожене'),
)


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=20 , choices=CATEGORY, null=True)
    quantity = models.PositiveIntegerField(null=True)


    def __str__(self):
        return (self.name)


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    market = models.ForeignKey(Profile, models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product} заказано {self.market.market}'
