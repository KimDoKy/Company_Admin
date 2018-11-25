# Generated by Django 2.1.2 on 2018-11-25 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CardComp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_company', models.CharField(max_length=10, verbose_name='카드사')),
            ],
            options={
                'verbose_name_plural': '카드사',
            },
        ),
        migrations.CreateModel(
            name='PayBank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_money', models.CharField(max_length=14, verbose_name='입금금액')),
                ('bank_name', models.CharField(max_length=10, verbose_name='입금은행')),
                ('bank_in_name', models.CharField(max_length=10, verbose_name='입금자명')),
                ('bank_date', models.DateField(verbose_name='입금일')),
            ],
            options={
                'verbose_name_plural': '현금결제',
            },
        ),
        migrations.CreateModel(
            name='PayCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_sell', models.CharField(max_length=14, verbose_name='판매금액')),
                ('card_num', models.CharField(max_length=20, verbose_name='카드번호')),
                ('card_sell_date', models.DateField(verbose_name='결제일')),
                ('card_life', models.CharField(max_length=8, verbose_name='카드유효기간')),
                ('card_approval_num', models.CharField(max_length=10, verbose_name='승인번호')),
                ('card_plan', models.IntegerField(verbose_name='할부개월수')),
                ('card_money', models.CharField(max_length=14, verbose_name='결제금액')),
                ('card_comp', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='payments.CardComp', verbose_name='카드사')),
            ],
            options={
                'verbose_name_plural': '카드결제',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pmt_money', models.IntegerField(verbose_name='결제금액')),
                ('pmt_sell', models.IntegerField(blank=True, null=True, verbose_name='판매금액')),
                ('pmt_tax', models.IntegerField(blank=True, null=True, verbose_name='부가세')),
            ],
            options={
                'verbose_name_plural': '결제',
            },
        ),
        migrations.CreateModel(
            name='PaymentComp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=10, unique=True, verbose_name='승인회사')),
            ],
            options={
                'verbose_name_plural': '승인회사',
            },
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pmt_mtd', models.CharField(choices=[('card', '카드'), ('bank', '현금')], max_length=10, verbose_name='결제수단')),
                ('pmt_bank', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='payments.PayBank', verbose_name='현금결제')),
                ('pmt_card', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='payments.PayCard', verbose_name='카드결제')),
            ],
            options={
                'verbose_name_plural': '결제수단',
            },
        ),
        migrations.AddField(
            model_name='payment',
            name='pmt_comp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='payments.PaymentComp', verbose_name='승인회사'),
        ),
        migrations.AddField(
            model_name='payment',
            name='pmt_method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='payments.PaymentMethod', verbose_name='결제수단'),
        ),
    ]