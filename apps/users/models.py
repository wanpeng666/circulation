from django.db import models
from django.utils import timezone

from apps.guessNum.models import GameNumberModel


class Users(models.Model):
    """用户"""
    name = models.CharField(max_length=50, verbose_name='用户名', blank=True)
    mobile = models.CharField(max_length=11, verbose_name='手机', blank=True)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'

    def __str__(self):
        return self.name


class Player(models.Model):
    user = models.ForeignKey(Users, verbose_name='玩家', on_delete=True)
    game = models.ForeignKey(GameNumberModel, verbose_name='GameNum', on_delete=True)
    isWinner = models.BooleanField(default=False, verbose_name='是否为赢家')

    class Meta:
        verbose_name = '玩家'
        verbose_name_plural = '玩家'

    def __str__(self):
        return self.user.name


class PlayerGuessNums(models.Model):
    num = models.IntegerField(verbose_name='所猜数字')
    player = models.ForeignKey(Player, verbose_name='player', on_delete=True)
    time = models.DateTimeField(default=timezone.now, verbose_name='时间')

    class Meta:
        verbose_name = '所猜数字'
        verbose_name_plural = '所猜数字'

    def __str__(self):
        return self.num
