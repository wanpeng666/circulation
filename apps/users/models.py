import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from django.conf import settings


# Create your models here.
from django.utils import timezone

from apps.guessNum.models import GameNumberModel


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


class Player(models.Model):
    user = models.ForeignKey(User, verbose_name='用户名', on_delete=True)
    game = models.ForeignKey(GameNumberModel, verbose_name='GameNum', on_delete=True)


class PlayerGuessNums(models.Model):
    num = models.IntegerField(verbose_name='所猜数字')
    player = models.ForeignKey(Player, verbose_name='player', on_delete=True)
    time = models.DateTimeField(default=timezone.now, verbose_name='时间')
