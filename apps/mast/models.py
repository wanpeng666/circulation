from django.db import models
from django.utils import timezone

from apps.users.models import Users


class incidents(models.Model):
    reporter = models.ForeignKey(Users, max_length=15, verbose_name='报障人', blank=True, on_delete=True,
                                 related_name='reporter')
    status_choice = (
        ('1', '未受理'),
        ('2', '待接受'),
        ('3', '受理中'),
        ('4', '已解决'),
        ('5', '已关闭'),
    )
    status = models.CharField(max_length=3, choices=status_choice, verbose_name='状态', blank=True, default='1')
    title = models.CharField(max_length=150, verbose_name='标题', blank=True)
    levelChoice = (
        ('1', '一'),
        ('2', '二'),
        ('3', '三'),
        ('4', '四'),
        ('5', '五'),
    )
    level = models.CharField(max_length=5, verbose_name='事件等级', choices=levelChoice, default='4')
    emergencyChoice = (
        ('1', '紧急'),
        ('2', '高'),
        ('3', '中'),
        ('4', '低'),
    )
    degree = models.CharField(max_length=2, choices=emergencyChoice, verbose_name='紧急程度', blank=True)
    assigned_to = models.ForeignKey(Users, verbose_name='指派给', on_delete=True, null=True, blank=True,
                                    related_name='recived')
    sId = models.ForeignKey('self', verbose_name='源ID', on_delete=True, null=True, blank=True, related_name='source')
    islastest = models.BooleanField(verbose_name='是否最新', default=True)
    fId = models.ForeignKey('self', verbose_name='父ID', on_delete=True, null=True, blank=True, related_name='parent')
    Time = models.DateTimeField(verbose_name='时间', default=timezone.now, blank=True, null=True)
    solvedTime = models.DateTimeField(verbose_name='解决时间', blank=True, null=True)
    reason = models.CharField(max_length=200, verbose_name='拒绝理由', blank=True)

    class Meta:
        verbose_name = '事件工单'
        verbose_name_plural = '事件工单'

    def __str__(self):
        return str(self.id)
