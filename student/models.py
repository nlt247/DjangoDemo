from django.db import models
from django.utils.html import format_html
import datetime

class Account(models.Model):
    '''账户表'''
    #unique为不能为空
    username = models.CharField(max_length=64,unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    #auto_now_add 为自动创建添加时间
    register_date = models.DateTimeField(auto_now_add=True)
    #blank限制Admin中是否必填
    signature = models.CharField("签名",max_length=255,blank=True,null=True)
    #aritcle_set 表示Aritcle表的集合，可用.all()或.select_related()查出Aritcle中所有关联的数据

    #自定义显示
    def __str__(self):
        return self.username

    class Meta:
        #verbose_name = '用户'
        verbose_name_plural = '用户'

class Aritcle(models.Model):
    '''文章表'''
    title = models.CharField(max_length=255,unique=True)
    content = models.TextField()
    #CASCADE 关联删除
    #PROTECT 需要删除所有子对象
    #SET_NULL 主对象为空
    #SET_DEFAULT 默认给指定用户
    account = models.ForeignKey('Account',on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag',null=True,blank=True)
    pub_date = models.DateTimeField(default=datetime.datetime.now())
    read_count = models.CharField(max_length=255,null=True)

    def get_tags(self):
        names = ','.join([i.name for i in self.tags.all()])
        return format_html('<span style="color:red;" >{}</span>',names)

    def get_comment(self):
        return 10

    def __str__(self):
        return '%s - %s' % (self.id, self.title)

class Tag(models.Model):
    '''标签表'''
    name = models.CharField(max_length=64,unique=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name