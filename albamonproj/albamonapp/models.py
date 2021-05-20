#DB에 저장되는 데이터
from django.db import models

# Create your models here.

class Alba(models.Model):
    title = models.CharField(max_length = 100)
    writer = models.CharField(max_length = 200)
    pub_date = models.DateTimeField()
    adress = models.CharField(max_length = 30)
    wage = models.IntegerField()
    body = models.TextField()
    applicant = models.IntegerField(default = 0)

    #admin 페이지에 타이틀이름으로
    def __str__(self):
        return self.title

