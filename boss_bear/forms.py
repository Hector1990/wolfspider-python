from django import forms

SEX_CHOICES = (("男", "男"), ("女", "女"))

class EmployeeForm(forms.Form):
    name = forms.CharField(label='姓名', max_length=30, required=True)
    id_card_number = forms.CharField(label='身份证号码', max_length=30, required=True)
    mobile_number = forms.IntegerField(label="手机", required=True)
    sex = forms.ChoiceField(choices=SEX_CHOICES)
    age = forms.IntegerField(label="年龄", required=False)
    nationality = forms.CharField(label="民族", max_length=20, required=True)
