# Generated by Django 2.1.2 on 2018-11-26 13:30

import accounts.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('custom_username', models.CharField(max_length=20, unique=True, verbose_name='아이디')),
                ('name', models.CharField(max_length=10, verbose_name='이름')),
                ('level', models.CharField(choices=[('lv1', '사원'), ('lv2', '주임'), ('lv3', '대리'), ('lv4', 'MD'), ('lv5', '팀장'), ('lv6', '과장'), ('lv7', '실장'), ('lv8', '본부장'), ('lv9', '차장'), ('lv10', '부장'), ('lv11', '이사'), ('lv12', '대표이사')], max_length=20, verbose_name='직급')),
                ('number', models.CharField(blank=True, max_length=14, verbose_name='전화번호')),
                ('phone', models.CharField(blank=True, max_length=14, verbose_name='휴대폰번호')),
                ('birth', models.DateField(blank=True, null=True, verbose_name='생년월일')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
            options={
                'verbose_name_plural': '사용자',
            },
            managers=[
                ('objects', accounts.models.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_code', models.CharField(auto_created=True, max_length=10, verbose_name='부서코드')),
                ('team_name', models.CharField(max_length=10, verbose_name='부서명')),
                ('team_deps', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Team', verbose_name='상위부서')),
            ],
            options={
                'verbose_name_plural': '부서',
            },
        ),
        migrations.AddField(
            model_name='customuser',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.Team', verbose_name='부서'),
        ),
    ]
