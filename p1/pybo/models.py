from django.db import models
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.fields import EmailField
from datetime import datetime
import hashlib


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, request, user_name=None, phone=None, company_name=None, password=''):
        if not request.POST['email']:
            raise ValueError('잘못된 접근입니다.')
        
        user = self.model(
            email = self.normalize_email(request.POST['email']),
            user_name = user_name,
            reg_date = datetime.today().strftime('%Y-%m-%d') +' '+ datetime.today().strftime('%H:%M:%S'),
            user_type = 'U2',     # default : 무료 가입자(U2) 설정
            is_active = 0,
            phone = phone,
            company_name = company_name
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    def update_user(self, request):
        user = get_user_model().objects.get(email=request.POST['email'])

        user.user_name = request.POST['user_name']
        user.phone = request.POST['phone']
        user.company_name = request.POST['company_name']
        user.set_password(request.POST['password'])
        user.save(using=self._db)
        return user
class UserAuth(object):
    def authenticate(**kwargs):
        username = kwargs.get('username')
        password = kwargs.get('password')

        try:
        	user = get_user_model().objects.get(email=email)
        except:
            # 유저가 존재하지 않음
            return None
        '''
        if user.status == 'LOCKED':
            # 유저 상태가 잠금인 경우
            raise Exception('USER IS LOCKED')
            
        if user.login_fail_count >= 5:
            # 로그인 실패 횟수가 5회 이상이면 로그인 불가
            raise Exception('PASSWORD FAILED BY 5 TIMES')
        '''
        if str(user.password) == hashlib.sha256(password.encode('utf-8')).hexdigest():
            # 패스워드 일치 => 로그인 성공
            #user.login_fail_count = 0 # 패스워드 실패 횟수를 0으로 초기화
            #user.save(update_fields=['login_fail_count'])
            return user
        else:
            # 패스워드 불일치 => 로그인 실패
            #user.login_fail_count += 1
            #user.save(update_fields=['login_fail_count'])
            return None
class User(AbstractBaseUser):
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    reg_date = models.DateTimeField(blank=True, null=True)
    user_type = models.CharField(max_length=2)
    user_name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=20, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    company_name = models.CharField(max_length=100, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']
    class Meta:
        db_table= 'User'

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def set_password(self, password):
    	self.password = hashlib.sha256(password.encode('utf-8')).hexdigest()


class UserAuth(object):
    def authenticate(**kwargs):
        email = kwargs.get('email')
        password = kwargs.get('password')

        try:
        	user = get_user_model().objects.get(email=email)
        except:
            # 유저가 존재하지 않음
            return None
        '''
        if user.status == 'LOCKED':
            # 유저 상태가 잠금인 경우
            raise Exception('USER IS LOCKED')
            
        if user.login_fail_count >= 5:
            # 로그인 실패 횟수가 5회 이상이면 로그인 불가
            raise Exception('PASSWORD FAILED BY 5 TIMES')
        '''
        if str(user.password) == hashlib.sha256(password.encode('utf-8')).hexdigest():
            # 패스워드 일치 => 로그인 성공
            #user.login_fail_count = 0 # 패스워드 실패 횟수를 0으로 초기화
            #user.save(update_fields=['login_fail_count'])
            return user
        else:
            # 패스워드 불일치 => 로그인 실패
            #user.login_fail_count += 1
            #user.save(update_fields=['login_fail_count'])
            return None

class Funding(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='작성자', db_column='writer')
    point = models.PositiveIntegerField(default=0, verbose_name='포인트')
    balance = models.PositiveIntegerField(default=0, verbose_name='잔액')
    class Meta:
        db_table= 'funding'
class Writing(models.Model):
    title = models.CharField(max_length=64,verbose_name="글제목")
    contents = models.TextField(verbose_name="글내용")
    userid = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='작성자', db_column='writerid')
    tag = models.CharField(max_length=32,verbose_name='게시판종류')
    write_dttm = models.DateTimeField(auto_now=True, verbose_name='마지막수정일')
    hits = models.PositiveIntegerField(default=0, verbose_name='조회수')
    capital = models.PositiveIntegerField(default=0,verbose_name='펀딩금액')
    class Meta:
        db_table = 'writing'
            
    def __str__(self):
        return self.title


