from django.db import models
from django.contrib.auth.models import AbstractUser

class Team(models.Model):
    team_1 = models.CharField(max_length=20)
    team_2 = models.ForeignKey('accounts.Team', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        if self.team_2:
            return f'[{self.team_2}] - [{self.team_1}]'
        else:
            return f'[{self.team_1}]'


class CustomUser(AbstractUser):
    SELECT_LV = (
            ('lv1','사원'),
            ('lv2','주임'),
            ('lv3','대리'),
            ('lv4','MD'),
            ('lv5','팀장'),
            ('lv6','과장'),
            ('lv7','실장'),
            ('lv8','본부장'),
            ('lv9','차장'),
            ('lv10','부장'),
            ('lv11','이사'),
            ('lv12','대표이사'),
            )
    name = models.CharField(max_length=10)
    team = models.ForeignKey('Team', blank=True, null=True, on_delete=models.PROTECT)
    level = models.CharField(max_length=20, choices=SELECT_LV)
    number = models.CharField(max_length=14, blank=True)
    phone = models.CharField(max_length=14, blank=True)
    birth = models.DateField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f'{self.username}'
