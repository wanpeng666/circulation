from django.db import models

from apps.users.models import Player


class GameNumberModel(models.Model):
    num = models.IntegerField(verbose_name='GameNum')
    statusChoice= (
        (1, '进行中'),
        (2, '已结束')
    )
    status = models.CharField(max_length=3, verbose_name='游戏状态', default=1)
    winner = models.ForeignKey(Player, verbose_name='获胜者', on_delete=True, blank=True, null=True)