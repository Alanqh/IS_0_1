from django.db import models
from django.contrib.auth.models import AbstractUser


class Car(models.Model):
    car_id = models.CharField(max_length=20, primary_key=True)
    car_name = models.CharField('车名', max_length=50)

    # 添加其他汽车相关的字段
    def __str__(self):
        return self.car_name


class User(AbstractUser):
    ROLE_CHOICES = (
        ('customer', '客户'),
        ('staff', '员工'),
    )
    role = models.CharField('角色', max_length=10, choices=ROLE_CHOICES)
    department = models.CharField('部门', max_length=50)
    last_name = models.CharField('姓', max_length=50)
    first_name = models.CharField('名', max_length=50)
    gender = models.CharField('性别', max_length=10)
    birth_date = models.DateField('出生年月')
    email = models.EmailField('邮箱')
    phone_number = models.CharField('手机号', max_length=20)

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="custom_user_set",  # 指定不同的related_name
        related_query_name="custom_user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="custom_user_set",  # 指定不同的related_name
        related_query_name="custom_user",
    )

    def __str__(self):
        return self.username
