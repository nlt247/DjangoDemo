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
    #每页显示数量默认20行
    list_per_page = 20
    #设置通过哪个字段跳转修改
    #list_display_links = ('email',)

    #设置直接在列表上可更改的字段
    list_editable = ['signature']

class AritcleAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date','account','get_tags')

    #设置右边栏的分组
    list_filter = ('title','pub_date')

    #设置详情页可修改字段,使用()让字段显示在同一行
    #exclude = () 为不显示某些字段
    #fields = ('title','pub_date',('pub_date','read_count'))

    #按日期分组
    date_hierarchy = 'pub_date'

    #fieldsets分组显示,fieldsets与fields只能存在一个
    #classes设置样式wide和coolapse是自带的
    fieldsets = (
        ('文章内容',{
            'fields':('title','content'),
            'classes':('wide','extrapretty')
        }),
        ('发布相关',{
            'fields':('account','pub_date','tags','read_count'),
            'classes':('coolapse')
        })
    )

    #针对多对多选择进行优化 水平方向
    filter_horizontal = ['tags']
    #垂直方向
    #filter_vertical = ('tags')

    #设置字段为radio按钮,VERTICAL为纵向,HORIZONTAL为横向
    #radio_fields = {'acount': admin.HORIZONTAL}

    #自动补全(此项好像与fieldsets冲突)
    autocomplete_fields = ['account']
    #该字段与autocomplete_fields冲突,可打开选项进行选择
    #raw_id_fields = ['account']

    #设置只读字段
    readonly_fields = ['read_count']

class TagAdmin(admin.ModelAdmin):
    list_display = ('name','date')

#将定制内容添加到对应表
admin.site.register(models.Account,AccountAdmin)
admin.site.register(models.Aritcle,AritcleAdmin)
admin.site.register(models.Tag,TagAdmin)