from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest


class YearsExperienceSalaryMiddleware(MiddlewareMixin):
    def process_requested(self, request):
        if request.path == '/workregister/' and request.method == 'POST':
            years_of_experience = int(request.POST.get('years_of_experience'))
            if years_of_experience <= 1:
                return HttpResponseBadRequest('Ваш опыт слишком мал для регистрации')
            elif years_of_experience >=2 and years_of_experience <= 3:
                request.salary = 1000
            elif years_of_experience >=4 and years_of_experience <= 5:
                request.salary = 2000
            elif years_of_experience > 6:
                request.salary = 3000
            else:
                return HttpResponseBadRequest('Ваш опыт слишком мал для регистрации')
        elif request.path == '/workregister/' and request.method == 'POST':
            setattr(request, 'salary', 'Зарплата не определено')
