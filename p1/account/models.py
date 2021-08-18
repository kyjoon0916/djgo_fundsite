import hashlib
from datetime import datetime
from django.conf import settings
from django.contrib.auth import get_user_model, login, authenticate
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.sessions.models import Session
from django.db import models
from django.db.models.fields import EmailField


# class IntegerRangeField(models.IntegerField):
#     def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
#         self.min_value, self.max_value = min_value, max_value
#         models.IntegerField.__init__(self, verbose_name, name, **kwargs)
#     def formfield(self, **kwargs):
#         defaults = {'min_value': self.min_value, 'max_value':self.max_value}
#         defaults.update(kwargs)
#         return super(IntegerRangeField, self).formfield(**defaults)


class UserManager(BaseUserManager):
    def create_user(self, email, user_name=None, password=''):
        if email == '':
            raise ValueError('잘못된 접근입니다.')
        
        user = self.model(
            email = self.normalize_email(email),
            user_name = user_name,
            reg_date = datetime.today().strftime('%Y-%m-%d') +' '+ datetime.today().strftime('%H:%M:%S'),
            is_active = 0,
        )
        print('create_user is invoked')
        print('password=', password)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password
        )
        user.is_active = 1
        user.is_admin = True
        user.save(using=self._db)
        return user


    def update_user(self, request):
        user = get_user_model().objects.get(email=request.POST['email'])

        user.user_name = request.POST['email']
        user.set_password(request.POST['password'])
        user.save(using=self._db)
        return user

    
    def delete_user(self, email):
        response_data = {}
        try:
            get_user_model().objects.filter(email=email).delete()
        except Exception as e:
            response_data['message'] = e
        else:
            response_data['message'] = 'ok'
        return response_data


class UserAuth(object):
    # def __init__(self, **kwargs):
        # print('UserAuth is invoked')
    def authenticate(self, **kwargs):
        print('UserAuth.authenticate is invoked')
        
        email = kwargs.get('email')
        print('email=', email)
        password = kwargs.get('password')
        print('password=', password)

        try:
        	user = get_user_model().objects.get(email=email)
            # get --> filter
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

        # if str(user.password) == hashlib.sha256(password.encode('utf-8')).hexdigest():
        if user.check_password(password):

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
    user_name = models.CharField(max_length=100, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    balance = models.IntegerField(default=50000000, editable=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        print('is_staff is invoked')
        print('self.is_admin=', self.is_admin)
        return self.is_admin

    # def set_password(self, password):
    # 	self.password = hashlib.sha256(password.encode('utf-8')).hexdigest()

