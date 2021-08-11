from django.db import models
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.fields import EmailField
from datetime import datetime
import hashlib


# Create your models here.



class Writing(models.Model):
    title = models.CharField(max_length=64,verbose_name="글제목")
    contents = models.CharField(max_length=255,verbose_name="글내용")
    userid = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='작성자', db_column='writerid')
    tag = models.CharField(max_length=32,verbose_name='게시판종류')
    pub_date = models.DateTimeField('data published',default=datetime.now)
    capital = models.PositiveIntegerField(default=0,verbose_name='펀딩금액')
    class Meta:
        db_table = 'Writing'
        ordering = ['pub_date']
            
    def __str__(self):
        return self.title

class Funding(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='회원ID', db_column='funding_id')
    writing_id = models.ForeignKey(Writing, on_delete=models.CASCADE, verbose_name='글ID', db_column='writing_id')
    funding = models.PositiveIntegerField(default=0, verbose_name='투자금액')
    pub_date = models.DateTimeField('data published', default=datetime.now,)
    class Meta:
        db_table= 'funding'
