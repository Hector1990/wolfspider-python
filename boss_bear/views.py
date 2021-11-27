from django.http import HttpResponse
from django.template import loader
from django.views.generic import FormView
from .forms import EmployeeForm
from .models import Employee
from django.shortcuts import get_object_or_404, render

class EmployeeFormView(FormView):
    template_name = "index.html"
    form_class = EmployeeForm

def register(request):
    try:
        name = request.POST['name']
        id_card = request.POST['id_card_number']
        mobile = request.POST['mobile_number']
        sex = request.POST['sex']
        age = request.POST['age']
        nationality = request.POST['nationality']

        findIt = Employee.objects.filter(
            name = name,
            id_card_number=id_card,
            mobile_number=mobile
        )

        if findIt.exists():
            return render(request, 'result.html', {
                'msg_title': '重复提交',
                'error_message': '你已经提交过信息'
            })

        employee = Employee(
            name=name,
            id_card_number=id_card,
            mobile_number=mobile,
            sex=sex,
            age=age,
            nationality=nationality
        )
        employee.save()
        return render(request, 'result.html', {
            'msg_title': '提交成功',
            'happy_message': '提交成功'
        })
    except Exception:
        return render(request, 'result.html', {
            'msg_title': '提交失败',
            'error_message': '提交失败, 请检查信息后重新提交'
        })
    return HttpResponse("Success")
