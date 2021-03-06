from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Team(models.Model):
    team_code = models.CharField(max_length=10, auto_created=True, verbose_name='부서코드')
    team_name = models.CharField(max_length=10, verbose_name='부서명')
    team_deps = models.ForeignKey('accounts.Team', on_delete=models.CASCADE, null=True, blank=True, verbose_name='상위부서')

    class Meta:
        verbose_name_plural = '부서'

    def __str__(self):
        if self.team_deps:
            return f'{self.team_deps} - {self.team_name}'
        else:
            return f'[{self.team_name}]'

class CustomUserManager(BaseUserManager):
    def create_user(self, custom_username, password):
        user = self.model(custom_username=custom_username, password=password)
        user.set_password(password)
        user.is_staff = False
        user.is_superuser = False
        user.save(using=self._db)
        return user

    def create_superuser(self, custom_username, password):
        user = self.create_user(custom_username=custom_username, password=password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, custom_username):
        print(custom_username)
        return self.get(custom_username=custom_username)

class CustomUser(AbstractBaseUser):
    objects = CustomUserManager()
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
    custom_username = models.CharField(max_length=20, verbose_name='아이디', unique=True)
    USERNAME_FIELD = 'custom_username'
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    name = models.CharField(max_length=10, verbose_name='이름')
    team = models.ForeignKey('Team', blank=True, null=True, on_delete=models.PROTECT, verbose_name='부서')
    level = models.CharField(max_length=20, choices=SELECT_LV, verbose_name='직급')
    number = models.CharField(max_length=14, blank=True, verbose_name='전화번호')
    phone = models.CharField(max_length=14, blank=True, verbose_name='휴대폰번호')
    birth = models.DateField(blank=True, null=True, verbose_name='생년월일')
    email = models.EmailField(blank=True, null=True)

    class Meta:
        verbose_name_plural = '사용자'

    def __str__(self):
        return f'{self.custom_username}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def is_staff(self):
        return self.is_admin
