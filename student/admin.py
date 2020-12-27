from django.contrib import admin
from student import models

#表单定制
class AccountAdmin(admin.ModelAdmin):
    #添加需要显示的列
    list_display = ('username','email','signature')
    #添加查询，设置查询条件
    search_fields = ('username','email')
    #过滤，去重
    list_filter = ('email',)

class AritcleAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date')
    list_filter = ('title','pub_date')
    #设置详情页可修改字段
    fields = ('title','pub_date')

#将定制内容添加到对应表
admin.site.register(models.Account,AccountAdmin)
admin.site.register(models.Aritcle,AritcleAdmin)
admin.site.register(models.Tag)