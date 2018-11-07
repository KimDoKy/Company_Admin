from django.db import models

class Payment(models.Model):
    pmt_meney = models.CharField(max_length=14, verbose_name='결제금액')
    pmt_sell = models.IntegerField(blank=True, null=True, verbose_name='판매금액')
    pmt_tax = models.IntegerField(blank=True, null=True, verbose_name='부가세')
    pmt_comp = models.ForeignKey('PaymentComp', on_delete=models.PROTECT, verbose_name='승인회사')
    pmt_method = models.ForeignKey('PaymentMethod', on_delete=models.PROTECT, verbose_name='결제수단')

    # 결제금액을 입력하고 저장하면 자동으로 판매금액과 부가세를 계산해서 저장
    def save(self, *args, **kwargs):
        self.pmt_tax = int(self.pmt_money) / 11
        self.pmg_sell = int(self.pmt_poney) - self.pmt_tax
        super(Payment, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = '결제'

    def __str__(self):
        return f'{self.pmt_money}'

# 결제 승인회사
class PaymentComp(models.Model):
    company = models.CharField(max_length=10, unique=True, verbose_naem='승인회사')

    def __str__(self):
        return f'{self.company}'

    class Meta:
        verbose_name_plural = '승인회사'
