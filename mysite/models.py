from django.db import models

class News(models.Model):
    title = models.CharField(max_length=50)#標題(最多50字)
    pdate = models.DateTimeField(auto_now_add=True)#日期(自動加時間)
    def __str__(self):
        return self.title

class Animal(models.Model):
    aid = models.PositiveIntegerField()
    place = models.CharField(max_length=100)
    kind = models.CharField(max_length=20)
    sex = models.BooleanField(default=False)
    status = models.CharField(max_length=20, default="N/A")
    remark = models.CharField(max_length=200)
    update = models.DateField()
    album = models.CharField(max_length=400)
    def __str__(self):
        return "{}({})".format(self.place, self.kind)
# Create your models here.