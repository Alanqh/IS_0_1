from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.db.models.functions import datetime

from customer.models import ServiceRecord, ServiceType
from register.models import User, Car


class UserInfoForm(UserChangeForm):
    GENDER_CHOICES = (
        ('male', '男'),
        ('female', '女'),
    )
    gender = forms.ChoiceField(label='性别', choices=GENDER_CHOICES)

    # 隐藏password字段，因为我们将密码修改功能放在另一个页面
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()

    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'gender', 'birth_date', 'email', 'phone_number',
                  'username')
        labels = {
            'first_name': '名字',
            'last_name': '姓氏',
            'email': '电子邮件',
            'phone_number': '手机号',
            'birth_date': '出生日期',
            'gender': '性别',
            'username': '用户名',
        }
        widgets = {
            'username': forms.TextInput(attrs={'readonly': 'readonly'}),
        }


from django.contrib.auth.forms import PasswordChangeForm


class ChangePasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(self.user, *args, **kwargs)




class ServiceApplicationForm(forms.ModelForm):
    # 用户只能为自己申请售后服务，所以user默认为当前登录的客户
    user = forms.ModelChoiceField(label='用户', queryset=User.objects.filter(role='customer'), empty_label=None)
    service_type = forms.ModelChoiceField(label='服务类型', queryset=ServiceType.objects.all(), empty_label=None)
    car = forms.ModelChoiceField(label='车型', queryset=Car.objects.all(), empty_label=None)
    description = forms.CharField(label='描述', widget=forms.Textarea)
    datetime = forms.DateTimeField(
        label='申请时间',
        widget=forms.DateTimeInput(attrs={'type': 'datetime'}),
        initial=datetime.datetime.now()
    )
    service_state = forms.IntegerField(label='服务状态', initial=0, widget=forms.HiddenInput())

    class Meta:
        model = ServiceRecord
        fields = ['user', 'service_type', 'car', 'datetime', 'description', 'service_state']
