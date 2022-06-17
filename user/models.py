from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class UserManager(BaseUserManager):
    def create_user(self, email, username, type_id, password=None):
        if not username:
            raise ValueError('Users must have an username')

        type_obj = UserType.objects.get(id=type_id)
        user = self.model(
            email=email,
            username=username,
            type=type_obj
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    # python manage.py createsuperuser 사용 시 해당 함수가 사용됨
    def create_superuser(self, email, username, type_id, password=None):
        user = self.create_user(
            email=email,
            username=username,
            type_id=type_id,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class UserType(models.Model):
    type = models.CharField("유저 타입", max_length=50, unique=True)

    def __str__(self):
        return self.type

class User(AbstractBaseUser):
    type = models.ForeignKey(UserType, on_delete=models.CASCADE)
    username = models.CharField("사용자 아이디", max_length=12, unique=True)
    email = models.EmailField("이메일", max_length=100, unique=True)
    password = models.CharField("비밀번호", max_length=128)
    fullname = models.CharField('이름', max_length=20)
    join_date = models.DateTimeField('생성시각', auto_now_add=True)
    
    def __str__(self):
        return self.username

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'type_id']

    objects = UserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

