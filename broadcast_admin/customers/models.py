from django.db import models

class Customer(models.Model):
    adver_name = models.CharField(max_length=5, verbose_name='대표자')
    comp_name = models.CharField(max_length=20, verbose_name='상호명')
    comp_num = models.CharField(max_length=12, verbose_name='사업자번호')
    comp_uptae = models.CharField(max_length=15, verbose_name='업태')
    comp_upjong = models.CharField(max_length=20, verbose_name='업종')
    comp_post = models.CharField(max_length=10, verbose_name='우편번호')
    comp_addr = models.TextField(verbose_name='주소')
    comp_call = models.CharField(max_length=15, verbose_name='전화번호')
    comp_phone = models.CharField(max_length=15, verbose_name='휴대폰번호')
    comp_fax = models.CharField(max_length=15, verbose_name='팩스번호')
    comp_email = models.EmailField(verbose_name='이메일')
    comp_people = models.CharField(max_length=5, verbose_name='담당자')
    comp_url = models.TextField(verbose_name='URL')

    class Meta:
        verbose_name_plural = '고객사'

    def __str__(self):
        return f'{self.comp_name}'



