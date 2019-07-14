from django.db import models

# Create your models here.
# 用户表
class passcet_user(models.Model):
    name = models.CharField(max_length=30) #昵称
    email = models.CharField(max_length=60, null=True) #email 电话和邮件有一个即可
    phone = models.IntegerField(null=True) #电话号码
    leavel = models.IntegerField(null=False,default=0) #学习等级 0为未设置 4是band4 6是band6
    logintime = models.IntegerField(null=False,default=0) #最后一次登录时间，为了保持登录状态
    registertime = models.IntegerField(null=False,default=0) # 注册时间
    lastimei = models.IntegerField(null=True,default=0) #最后一次登录的设备特征号

#邮箱验证码
class passcet_emailcode(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.IntegerField()
    time = models.FloatField(default=0)