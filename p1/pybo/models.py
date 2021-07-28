from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Writing(models.Model):
    title = models.CharField(max_length=64,verbose_name="글제목")
    contents = models.TextField(verbose_name="글내용")
    username = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='작성자', db_column='username')
    tag = models.CharField(max_length=32,verbose_name='게시판종류')
    write_dttm = models.DateTimeField(auto_now=True, verbose_name='마지막수정일')
    hits = models.PositiveIntegerField(default=0, verbose_name='조회수')
    capital = models.PositiveIntegerField(default=0,verbose_name='펀딩금액')
    class Meta:
        db_table = 'writing'
            
    def __str__(self):
        return self.title

class Member(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='작성자', db_column='username')
    point = models.PositiveIntegerField(default=0, verbose_name='포인트')
    balance = models.PositiveIntegerField(default=0, verbose_name='잔액')
    class Meta:
        db_table= 'member'
