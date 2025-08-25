from django.shortcuts import render, redirect
from django.contrib import messages
from .models import TrainingRegistration

# Create your views here.
# Функция отвечает за рендер главной страницы (Запись на занятие) и отправку формы в базу данных
def registration(request):
    if request.method == 'POST':
        # Получаем данные из формы
        child_name = request.POST.get('child_name')
        birth_date = request.POST.get('birth_date')
        phone_number = request.POST.get('phone_number')
        planned_date = request.POST.get('planned_date')
        agreement = request.POST.get('agreement') == 'on'  # checkbox возвращает 'on' если отмечен
        
        # Сохраняем в базу
        try:
            registration = TrainingRegistration(
                child_name = child_name,
                birth_date = birth_date,
                phone_number = phone_number,
                planned_date = planned_date,
                agreement = agreement
            )
            registration.save()
            
            messages.success(request, 'Заявка успешно отправлена! Мы свяжемся с вами в ближайшее время.')
            return redirect('registration')
            
        except Exception as e:
            messages.error(request, f'Произошла ошибка: {str(e)}')
    
    return render(request, 'mySite/index.html')
    

def about(request):
    return render(request, 'mySite/about.html')

def help(requset):
    return render(requset, 'mySite/help.html')