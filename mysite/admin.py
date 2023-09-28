from django.contrib import admin
from mysite.models import News,Animal

@admin.register(News)#註冊
class NewsAdmin(admin.ModelAdmin):#納入管理
    list_display = ('title','pdate')
# Register your models here.

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('aid', 'place', 'kind', 'sex', 'status', 'remark', 'update')