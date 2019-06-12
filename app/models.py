from django.db import models
from django.contrib.auth.models import User, AbstractUser   # 导入 AbstractUser 类
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)


class UserProfileManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            name=name,
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='邮箱',
        max_length=255,
        unique=True,
        default='hj@qq.com',
    )
    name = models.CharField(max_length=64, verbose_name='姓名')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    detail = models.OneToOneField('UserDetail', verbose_name='员工详细', on_delete=models.CASCADE, blank=True, null=True)
    role = models.ManyToManyField('Role', blank=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.get_username()

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    class Meta:
        verbose_name_plural = '用户表'
        permissions = (
            ('app_staff_detail', '可以查看员工个人信息的数据'),
            ('app_fina_state', '可以查看财务报表'),
            ('app_payroll', '可以查看工资条'),


        )


class Role(models.Model):
    """角色表"""
    name = models.CharField(max_length=64, verbose_name='角色名字', unique=True)
    menus = models.ManyToManyField("Menus", blank=True, null=True)

    class Meta:
        verbose_name_plural = '角色表'

    def __str__(self):
        return self.name


class Menus(models.Model):
    """动态菜单表"""
    name = models.CharField(max_length=64, verbose_name='菜单名称')
    # url_type_choices = ((0, 'absolute'), (1, 'dynamic'))
    # url_type = models.SmallIntegerField(choices=url_type_choices, verbose_name='菜单类型（固定|动态）', default=0)
    url_name = models.CharField(max_length=128, verbose_name='url 地址')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '菜单表'
        unique_together = ('name', 'url_name')


class UserDetail(models.Model):
    """员工个人信息"""
    sex_choices = ((0, '男'), (1, '女'))
    sex = models.PositiveSmallIntegerField(choices=sex_choices, default=0, verbose_name='性别')
    height = models.FloatField(max_length=4, verbose_name='身高', blank=True, null=True)

    is_married = ((0, '否'), (1, '是'))
    marriy = models.PositiveSmallIntegerField(choices=is_married, default=0, verbose_name='是否已婚', blank=True, null=True)
    phone = models.CharField(max_length=11, verbose_name='手机号码', blank=True, null=True)
    addr = models.CharField(max_length=128, verbose_name='家庭地址', blank=True, null=True)

    def __str__(self):
        return '%s-%s' % (self.sex, self.height)

    class Meta:
        verbose_name_plural = '员工信息表'

