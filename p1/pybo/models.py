from django.db import models
# from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.fields import EmailField
from datetime import datetime
from account.models import User




class Writing(models.Model):
    title = models.CharField(max_length=64,verbose_name="제목")
    contents = models.TextField(verbose_name="내용")
    writer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='작성자')
    tag = models.CharField(max_length=32,verbose_name='태그')
    pub_date = models.DateTimeField(default=datetime.now)
    img_file_name = models.CharField(max_length=64,verbose_name='이미지파일')
    accumulated_amount = models.PositiveIntegerField(default=0,verbose_name='펀딩금액', editable=True)
    
    class Meta:
        db_table = 'writing'
        ordering = ['pub_date']
        verbose_name = '아이디어 펀딩'
        verbose_name_plural = '아이디어 펀딩'    
    def __str__(self):
        return self.title


class FundingLog(models.Model):
    funding_id = models.BigIntegerField(blank=True, null=False, primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    writing_id = models.ForeignKey(Writing, on_delete=models.CASCADE, db_column='writing_id')
    funding_amount = models.IntegerField(null=True)
    funding_date = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table= 'funding_log'


