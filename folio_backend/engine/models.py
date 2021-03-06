from datetime import timedelta

from django.conf import settings
from django.db import models


class Follow(models.Model):
    # id = models.BigIntegerField(primary_key = True)
    portfolio = models.ForeignKey("Portfolio", models.CASCADE, db_column="portfolio")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, db_column="user")
    starttime = models.DateTimeField()
    # endtime = models.DateTimeField()
    budget = models.FloatField()
    # cash = models.FloatField()
    # stop_limit = models.FloatField()
    is_alive = models.BooleanField(default=True)

    class Meta:
        managed = True
        db_table = "follow"
        # unique_together = (("portfolio", "user"),)


class Portfolio(models.Model):
    # id = models.BigIntegerField(primary_key = True)
    name = models.TextField(default="我是一個投資組合")
    description = models.TextField(default="世界你好")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, db_column="owner")
    follow_price = models.FloatField(default=1000, blank=True)
    budget = models.FloatField(default=10000, blank=True)
    is_public = models.BooleanField(default=False)
    is_alive = models.BooleanField(default=True)

    class Meta:
        managed = True
        db_table = "portfolio"

    @property
    def num_follower(self):
        return self.follow_set.all().filter(is_alive=True).count()


class Stock(models.Model):
    # id = models.AutoField(primary_key = True)
    code = models.TextField()
    name = models.TextField()
    group = models.TextField()

    class Meta:
        managed = True
        db_table = "stock"

    @property
    def last_day_change(self):
        price_last_time = self.price.last().time
        price_last_second = self.price.get(time=price_last_time - timedelta(days=1)).price
        price_last = self.price.last().price
        return (price_last - price_last_second) / price_last

    def last_price(self):
        return self.price.last().price


class Stockprice(models.Model):
    # id = models.BigIntegerField(primary_key = True)
    stock = models.ForeignKey(Stock, models.CASCADE, db_column="stock", related_name="price")
    time = models.DateTimeField()
    price = models.FloatField()

    class Meta:
        managed = True
        db_table = "stockprice"
        # unique_together = (("stock", "time"),)


class Transaction(models.Model):
    # id = models.BigIntegerField(primary_key = True)
    portfolio = models.ForeignKey(Portfolio, models.CASCADE, db_column="portfolio")
    stock = models.ForeignKey(Stock, models.CASCADE, db_column="stock")
    amount = models.FloatField()
    time = models.DateTimeField()
    price = models.FloatField()

    class Meta:
        managed = True
        db_table = "transaction"
        # unique_together = (("portfolio", "stock"),)
