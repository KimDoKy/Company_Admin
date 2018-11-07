from django.contrib import admin
from .models import *

admin.site.register(Payment)
admin.site.register(PaymentComp)
admin.site.register(PaymentMethod)
admin.site.register(PayCard)
admin.site.register(CardComp)
admin.site.register(PayBank)
