from django.contrib import admin
from django.contrib.humanize.templatetags.humanize import intcomma
from .models import *

class PaymentAdmin(admin.ModelAdmin):
    fields = ['pmt_money','pmt_comp','pmt_method']
    list_display = ['pmt_sell_comma',]

    def pmt_sell_comma(self, payment):
        c = intcomma(payment.pmt_sell)
        return c 

admin.site.register(Payment, PaymentAdmin)
admin.site.register(PaymentComp)
admin.site.register(PaymentMethod)
admin.site.register(PayCard)
admin.site.register(CardComp)
admin.site.register(PayBank)
