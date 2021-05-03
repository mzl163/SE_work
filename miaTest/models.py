from django.db import models

# Create your models here.
class user(models.Model):
    user_id = models.CharField(max_length=11, primary_key=True)
    user_password = models.CharField(max_length=20)
    user_phone = models.CharField(max_length=11)

class commodity(models.Model):
    co_id = models.CharField(max_length=5,primary_key=True)
    co_name = models.CharField(max_length=5)
    co_src = models.URLField(max_length=200)
    co_price = models.FloatField()
    co_num = models.IntegerField()

class order(models.Model):
    user_id = models.ForeignKey('user',on_delete=models.CASCADE,null=True)
    co_id = models.ForeignKey('commodity',on_delete=models.CASCADE,null=True)
    order_time = models.DateTimeField()
    order_num = models.IntegerField()
    user_phone = models.CharField(max_length=11)

class shopping(models.Model):
    user_id = models.ForeignKey('user',on_delete=models.CASCADE,null=True)
    co_id = models.ForeignKey('commodity',on_delete=models.CASCADE,null=True)
    co_name = models.CharField(max_length=5)

class sales(models.Model):
    co_id = models.ForeignKey('commodity',on_delete=models.CASCADE,null=True)
    co_name = models.CharField(max_length=5)
    sales_num = models.IntegerField()

class admin(models.Model):
    ad_id = models.CharField(max_length=6,primary_key=True)
    ad_password = models.CharField(max_length=20)

class ad_active(models.Model):
    ad_ac = models.CharField(max_length=20, primary_key=True)