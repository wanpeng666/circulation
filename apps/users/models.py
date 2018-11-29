from django.db import models
from django.contrib.auth.models import AbstractUser

# from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from django.conf import settings


# Create your models here.
class BaseModel(models.Model):
    """为模型类补充字段"""
    # 数据的创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    # 数据的更新时间
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        abstract = True  # 说明抽象模型类


class User(AbstractUser, BaseModel):
    """用户"""
    mobile = models.CharField(max_length=11, verbose_name='手机', blank=True)
    avatar = models.ImageField(verbose_name='头像', blank=True, null=True)

    class Meta:
        db_table = "df_users"
