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

# 결제 수단
class PaymentMethod(models.Model):
    PAY_METHOD = (
            ('card','카드'),
            ('bank','현금'),
            )
    pmt_mtd = models.CharField(max_length=10, choices=PAY_METHOD, verbose_name='결제수단')
    pmt_card = models.ForeignKey('PayCard', on_delete=models.PROTECT, blank=True, null=True, verbose_name='카드결제')
    pmt_bank = models.ForeignKey('PayBank', on_delete=models.PROTECT, blank=True, null=True, verbose_name='현금결제')

    class Meta:
        verbose_name_plural = '결제수단'

    def get_method(self):
        if self.pmt_mtd == 'card':
            return self.pmt_card
        else:
            return self.pmt_bak

    def __str__(self):
        return f'{self.pmt_mtd}'


# 카드 결제
class PayCard(models.Model):
    card_sell = models.CharField(max_length=14, verbose_name='판매금액')
    card_comp = models.ForeignKey('CardComp', on_delete=models.PROTECT, verbose_name='카드사')
    card_num = models.CharField(max_length=20, verbose_name='카드번호')
    card_sell_date = models.DateField(verbose_naem='결제일')
    card_life = models.CharField(max_length=8, verbose_name='카드유효기간')
    card_approval_num = models.CharField(max_length=10, verbose_name='승인번호')
    card_plan = models.IntegerField(verbose_name='할부개월수')
    card_money = models.CharField(max_length=14, verbose_name='결제금액')

    class Meta:
        verbose_name_plural = '카드결제'

    def __str__(self):
        return f'{self.card_sell}'


# 카드사
class CardComp(models.Model):
    card_company = models.CharField(max_length=10, verbose_naem='카드사')

    class Meta:
        verbose_name_plural = '카드사'

    def __str__(self):
        return f'{self.card_company}'


# 현금 결제
class PayBank(models.Model):
    BANK_SELECT = (
            ()
            )
    bank_money = models.CharField(max_length=14, verbose_name='입금금액')
    bank_name = models.CharField(max_length=10, choices=BANK_SELECT, verbose_name='입금은행')
    bank_in_name = models.CharField(max_length=10, verbose_naem='입금자명')
    bank_date = models.DateField(verbose_name='입금일')

    class Meta:
        verbose_name_plural = '현금결제'

    def __str__(self):
        return f'{self.bank_name}'
