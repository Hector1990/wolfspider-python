from django.db import models

class Employee(models.Model):
    name = models.CharField("姓名", max_length=20)
    id_card_number = models.CharField("身份证", max_length=30)
    mobile_number = models.CharField("手机", max_length=20)
    sex = models.IntegerField("性别")
    nationality = models.CharField("民族", max_length=20)