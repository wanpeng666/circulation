from django.db import models
from django.utils import timezone


class GameNumberModel(models.Model):
    num = models.IntegerField(verbose_name='GameNum')
    statusChoice = (
        (1, '进行中'),
        (2, '已结束')
    )
    status = models.CharField(max_length=3, verbose_name='游戏状态', default=1)
    # winner = models.ForeignKey(Player, verbose_name='获胜者', on_delete=True, blank=True, null=True)
    createTime = models.DateTimeField(default=timezone.now, verbose_name='创建时间')
    endTime = models.DateTimeField(verbose_name='结束时间', blank=True, null=True)
